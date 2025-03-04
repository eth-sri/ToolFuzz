import abc


class EnvironmentImportMixin(abc.ABC):
    @abc.abstractmethod
    def _import_environment(self):
        """
        This method should import the environment for the agent to be run.
        If the environment is not imported, the agent will not work.
        """
        raise NotImplementedError
