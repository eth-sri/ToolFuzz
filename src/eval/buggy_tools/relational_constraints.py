from typing import List, Optional

from langchain_core.tools import tool
from langchain.pydantic_v1 import BaseModel, Field

from src.eval.buggy_tools.decorators import valid_prompt, breaking_prompt
from src.eval.toolfuzz.utils.assert_lambdas import assert_contains


class ItemPackagingInput(BaseModel):
    number_of_items: int = Field(description="The number of items that we want to be packaged")
    items: List[str] = Field(
        description="The names of the items that will be packages, NOTE: the number of item names MUST be equal to number_of_items parameter")


@valid_prompt(
    'I want to pack my custom alphabet of size 26. Please be careful to not scatter my alphabet: q, w, e, r, t, y, i, '
    'o, p, a, d, s, f, g, h, j, k, l, z, x, c, v, b, n, m, aa',
    lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, "Packed"))
@breaking_prompt(
    'I want to pack my custom alphabet of size 23. Please be careful to not scatter my alphabet: q, w, e, r, t, y, i, '
    'o, p, a, d, s, f, g, h, j, k, l, z, x, c, v, b, n, m, aa',
    lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, "Packed"))
@tool('package-items', args_schema=ItemPackagingInput, return_direct=True)
def package_items(number_of_items: int, items: List[str]):
    """
    Tool to be used when the user wants to package items together. The items can be of all sorts: computer files,
    clothing items, shoe pairs, planes etc.

    Below are few examples of the usage of the tool:
    Task: Can you pack the following 4 items: Milk, Cookies, Sandwich and Coca-Cola
    Tool usage: package_items(number_of_items=4, items=['Milk', 'Cookies', 'Sandwich', 'Coca-Cola'])

    Task: Can you pack the following 2 items: documents.pdf, invoice.xlsx
    Tool usage: package_items(number_of_items=2, items=['documents.pdf', 'invoice.xlsx'])

    Task: Please package these 5 items: League of legends, Dota 2, Minecraft, Raise of the Tomb Raider, Cities XL
    Tool usage: package_items(number_of_items=5, items=['League of legends', 'Dota 2', 'Minecraft', 'Raise of the Tomb Raider', 'Cities XL'])
    """

    assert number_of_items == len(items), \
        f"The number of items: {number_of_items} doesn't correspond to the presented items: {items}"

    return f'Packed {", ".join(items)}'


class AccountCreator(BaseModel):
    first_name: str = Field(description="The first name of the new employee")
    last_name: str = Field(description="The last name of the new employee")
    email: str = Field(description="Email of the new employee which has to start with the employee's last name")
    position: str = Field(description="The position which the new employee is: [SWE, HR, EXEC]")


@valid_prompt(
    "Next monday we have our new HR starting Regina Phalange can you create her mail phalange_regina@headhunters.com",
    lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, "The new account for"))
@breaking_prompt(
    "Next monday we have our new HR starting Regina Phalange can you create her mail regina.phalange@headhunters.com",
    lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, "The new account for"))
@tool('account-creator', args_schema=AccountCreator, return_direct=True)
def account_creator(first_name: str, last_name: str, email: str, position: str):
    """
    Tool for creating accounts for the new employees of the company. This tool can be used for setting up the new accounts for our employees.

    Below are few examples of the usage of the tool:
    Task: Please create new account for our new software engineer Ivan Milev with email milev.ivan@startup.com
    Tool usage: account_creator(first_name='Ivan', last_name='Milev', position='SWE', email='milev.ivan@startup.com')

    Task: Please create new account for our new software engineer Joe Doe with email doe_joe@gmail.com
    Tool usage: account_creator(first_name='Joe', last_name='Doe', position='SWE', email='doe_joe@gmail.com')
    """

    assert email.lower().startswith(last_name.lower()), f"The email has to start with the {last_name}"

    return (f"The new account for {first_name} {last_name} was successfully setup and will be active from tomorrow "
            f"with the {email} email")


# Sorting GraphQL style I guess
class MultiFieldSorting(BaseModel):
    item_type: str = Field(
        description="One of the following item types: ['tires', 'break system', 'suspension', 'lights', 'battery']")
    technology: str = Field(description="The technology used for the item, by default it is any")
    max_price: int = Field(description="The maximum price for an item allowed in the filter.")
    capacity: Optional[int] = Field(description="This field must be used only with item type: 'battery'")
    voltage: Optional[int] = Field(
        description="This field must be used only with item type: [battery, lights, break system]")
    radius: Optional[int] = Field(description="This field must be used only with item type: ['tires', 'break system']")
    max_carry: Optional[int] = Field(
        description="This field must be only used with item type: ['tires', 'suspension', break system]")
    max_speed: Optional[int] = Field(description="This field must be used only with item type: tires'")
    lumens: Optional[int] = Field(description="This field must be used only with item type: 'lights'")
    season: Optional[str] = Field(
        description="This field must be used only with item type: 'tires', valid values are: ['summer', 'winter', 'all-season']")


@valid_prompt(
    "Is there a suspension which is an air suspension which can carry my 2 ton truck and is less than 2 thousand dollars?",
    lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, "DWD-2318-213"))
@breaking_prompt(
    "Is there a suspension which is an air suspension which can carry my 2 ton truck and is less than 2 thousand dollars, my truck's top speed is 160 km/h?",
    lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, "DWD-2318-213"))
@tool('car-parts-filter', args_schema=MultiFieldSorting, return_direct=True)
def car_parts_filter(item_type: str, technology: str, max_price: int, capacity: Optional[int] = None,
                     voltage: Optional[int] = None,
                     max_speed: Optional[int] = None, max_carry: Optional[int] = None, lumens: Optional[int] = None,
                     radius: Optional[int] = None,
                     season: Optional[str] = None):
    """
    Tool which can filter car parts based on a different criteria. Useful when the user is search for car parts.

    Below are few examples of tasks and how the tool should be called for them:
    Task: I am looking for winter tires below 250 bucks for 20" rims.
    Tool call: car_parts_filter(item_type='tires', technology='any', season='winter', radius=20)

    Task: Are there batteries with capacity of 90 Ah with 6V below 200 USD
    Tool call: cap_parts_filter(item_type='battery',capacity=90, max_price=200, technology='any', voltage=6)

    Task: Can you find me headlights with 700 lumens below 20 CHF and for 6V socket, if possible halogens.
    Tool call: cap_parts_filter(lumens=700, max_price=20, voltage=6, technology='halogens')
    """

    # assert that none of the wrong filters is used
    if item_type == 'tires':
        assert capacity is None, f"Cannot filter for capacity for {item_type}"
        assert voltage is None, f"Cannot filter for voltage for {item_type}"
        assert radius is None, f"Cannot filter for radius for {item_type}"
        assert lumens is None, f"Cannot filter for lumens for {item_type}"
    elif item_type == 'break system':
        assert capacity is None, f"Cannot filter for capacity for {item_type}"
        assert max_speed is None, f"Cannot filter for maximum speed for {item_type}"
        assert lumens is None, f"Cannot filter for lumens for {item_type}"
        assert season is None, f"Cannot filter for season for {item_type}"
    elif item_type == 'suspension':
        assert capacity is None, f"Cannot filter for capacity for {item_type}"
        assert voltage is None, f"Cannot filter for voltage for {item_type}"
        assert radius is None, f"Cannot filter for radius for {item_type}"
        assert max_speed is None, f"Cannot filter for maximum speed for {item_type}"
        assert lumens is None, f"Cannot filter for lumens for {item_type}"
        assert season is None, f"Cannot filter for season for {item_type}"
    elif item_type == 'lights':
        assert capacity is None, f"Cannot filter for capacity for {item_type}"
        assert radius is None, f"Cannot filter for radius for {item_type}"
        assert max_carry is None, f"Cannot filter for maximum carry capacity for {item_type}"
        assert max_speed is None, f"Cannot filter for maximum speed for {item_type}"
        assert season is None, f"Cannot filter for season for {item_type}"
    elif item_type == 'battery':
        assert radius is None, f"Cannot filter for radius for {item_type}"
        assert max_carry is None, f"Cannot filter for maximum carry capacity for {item_type}"
        assert max_speed is None, f"Cannot filter for maximum speed for {item_type}"
        assert lumens is None, f"Cannot filter for lumens for {item_type}"
        assert season is None, f"Cannot filter for season for {item_type}"

    return "Yes, the part you are looking for is DWD-2318-213. It fits all your criteria."
