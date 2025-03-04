import inspect

from src.toolfuzz.tools.info_extractors.langchain_tool_wrapper import LangchainToolWrapper


class CrewAIToolWrapper(LangchainToolWrapper):

    def _import_environment(self):
        try:
            from crewai.tools import BaseTool
        except ImportError as e:
            error_msg = f"The crewai tools package is not installed. Please install it using 'pip install 'crewai[tools]''. {e}"
            raise ImportError(error_msg)

    def get_tool_docs(self):
        if 'description' in dir(self.tool):
            docs = self.tool.description
            if 'Tool Name:' in docs and 'Tool Arguments' in docs and 'Tool Description' in docs:
                return docs
            else:
                return self._generate_description()
        raise NotImplementedError("Only .description property is supported for now")

    def get_tool_src(self):
        if 'llama_index_tool' in dir(self.tool) and 'fn' in dir(self.tool.llama_index_tool):
            return inspect.getsource(self.tool.llama_index_tool.fn)
        else:
            return super().get_tool_src()

    def _generate_description(self):
        from crewai.tools import BaseTool

        """
        This method is used to generate the tool description. Directly lifted from:
        /lib/python3.10/site-packages/crewai/tools/base_tool.py
        :return: the tool description
        """
        args_schema = {
            name: {
                "description": field.description,
                "type": BaseTool._get_arg_annotations(field.annotation),
            }
            for name, field in self.tool.args_schema.model_fields.items()
        }

        return f"Tool Name: {self.get_tool_name()}\nTool Arguments: {args_schema}\nTool Description: {self.tool.description}"
