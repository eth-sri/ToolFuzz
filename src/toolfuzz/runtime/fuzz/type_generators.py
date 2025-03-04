import json
from typing import Protocol
from abc import abstractmethod

import sys
import random

from faker import Faker

from src.toolfuzz.runtime.fuzz.taints import TaintStr, TaintDict
from src.toolfuzz.tools.info_extractors.dataclasses import ArgumentType

Faker.seed(42)


class TypeGenerator(Protocol):
    @abstractmethod
    def generate(self, arg_type, next_gen=False): raise NotImplementedError

    @abstractmethod
    def can_gen(self, arg_type: ArgumentType) -> bool: raise NotImplementedError


class NullGenerator(TypeGenerator):
    def generate(self, arg_type, next_gen=False):
        return None

    def can_gen(self, arg_type: ArgumentType) -> bool:
        return arg_type.name.lower() == 'null'


class UnionGenerator(TypeGenerator):

    def __init__(self, upper_bound: int = 200):
        self.generators = [DictStrGenerator(), StringGenerator(), IntGenerator(),
                           FloatGenerator(), ListGenerator(), BooleanGenerator()]

    def generate(self, arg_type, next_gen=False):
        sub_type = random.choice(arg_type.sub_types)
        for generator in self.generators:
            if generator.can_gen(sub_type):
                return generator.generate(arg_type)

    def can_gen(self, arg_type: ArgumentType) -> bool:
        return arg_type.name.lower() == 'union'


class DictStrGenerator(TypeGenerator):
    def __init__(self, upper_bound: int = 200):
        self.upper_bound = upper_bound
        self.string_gen = StringGenerator(upper_bound)

    def generate(self, arg_type, next_gen=False):
        res_dict = {}
        for key in TaintDict.acc_keys:
            res_dict[key] = self.string_gen.generate(arg_type, next_gen)
        return json.dumps(res_dict)

    def can_gen(self, arg_type: ArgumentType) -> bool:
        # TODO: I should track the variables with @TaintStr
        type_str = arg_type.name
        return (type_str == 'string' or type_str == 'str' or type_str == str(str)) and len(TaintDict.acc_keys) != 0


class DictGenerator(TypeGenerator):

    def __init__(self, upper_bound: int = 200):
        self.upper_bound = upper_bound
        self.string_gen = StringGenerator(upper_bound)

    def generate(self, arg_type, next_gen=False):
        res_dict = {}
        for key in TaintDict.acc_keys:
            res_dict[key] = self.string_gen.generate(arg_type, next_gen)

    def can_gen(self, arg_type: ArgumentType) -> bool:
        type_str = arg_type.name
        return type_str == 'dict' or type_str == dict or type_str == str(dict)


class StringGenerator(TypeGenerator):
    def __init__(self, upper_bound: int = 500):
        self.upper_bound = upper_bound
        fakers = [Faker('en'), Faker('de'), Faker('bg_BG'), Faker('zh_CN')]
        self.string_gen = []
        for fake in fakers:
            self.string_gen.append(fake.address)
            self.string_gen.append(fake.name)
            self.string_gen.append(fake.text)
            self.string_gen.append(fake.email)
            self.string_gen.append(fake.bs)
            self.string_gen.append(fake.aba)
            self.string_gen.append(fake.emoji)
            self.string_gen.append(fake.administrative_unit)
        self.gen_iter = iter(self.string_gen)
        self.gen = next(self.gen_iter)

    def generate(self, arg_type, next_gen=False):
        if next_gen:
            try:
                self.gen = next(self.gen_iter)
            except StopIteration:
                pass
        sample = self.gen()
        if len(TaintStr.separators) != 0:
            for sep in TaintStr.separators:
                sample += sep + self.gen()
        if 'Provider.address' in str(self.gen):
            length = random.randint(1, self.upper_bound)
            while len(sample) < length:
                sample += ' ' + self.gen()
        return TaintStr(sample)

    def can_gen(self, arg_type: ArgumentType) -> bool:
        # TODO: I should track the @TaintStr and know if this variable here is dict or not
        type_str = arg_type.name
        return (type_str == 'string' or type_str == 'str' or type_str == str(str)) and len(TaintDict.acc_keys) == 0


class IntGenerator(TypeGenerator):
    def __init__(self, upper_bound=None):
        super().__init__()
        self.upper_bound = sys.maxsize if upper_bound is None else upper_bound

    def generate(self, arg_type, next_gen=False):
        return random.randint(0, self.upper_bound)

    def can_gen(self, arg_type: ArgumentType) -> bool:
        type_str = arg_type.name
        return type_str == 'integer'


class FloatGenerator(TypeGenerator):
    def __init__(self, upper_bound=None):
        self.upper_bound = sys.float_info.max if upper_bound is None else upper_bound

    def generate(self, arg_type, next_gen=False):
        return random.uniform(0, self.upper_bound)

    def can_gen(self, arg_type: ArgumentType) -> bool:
        type_str = arg_type.name
        return type_str == 'float' or type_str == 'number'


class BooleanGenerator(TypeGenerator):
    def __init__(self, upper_bound=None):
        pass

    def generate(self, arg_type, next_gen=False):
        return random.choice([True, False])

    def can_gen(self, arg_type: ArgumentType) -> bool:
        return arg_type.name.lower() == 'boolean'


class ListGenerator(TypeGenerator):
    def __init__(self, upper_bound=128):
        self.upper_bound = upper_bound
        self.generators = [StringGenerator, IntGenerator, FloatGenerator, NullGenerator, ListGenerator]

    def generate(self, arg_type, next_gen=False):
        generator = None
        for gen in self.generators:
            if gen().can_gen(arg_type.sub_types[0]):  # Lists have one subtype
                generator = gen()
                break
        assert generator is not None, f'No generator found for {arg_type}'
        length = random.randint(0, self.upper_bound)
        generated_list = []
        for _ in range(length):
            generated_list.append(generator.generate(arg_type, next_gen))
        return generated_list

    def can_gen(self, arg_type: ArgumentType) -> bool:
        type_str = arg_type.name
        return type_str == 'list' or type_str == 'array'


def get_generators():
    return [coi() for coi in TypeGenerator.__subclasses__()]
