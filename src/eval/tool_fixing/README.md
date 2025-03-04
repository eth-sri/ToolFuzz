## Automatic tool description fixing

In this package we present 3 scripts for fixing tools: 
1. `tool_fixer.py` - can fix a tool based on just the tool description; on the tool description and tool source code; tool description and a list of bad examples found by ToolFuzz
2. `fix_file_toolkit.py` - utility script which will go over the file toolkit tools and use ToolFixer to fix their description.
3. `github_toolkit_fixer.py` - utility script which will go over the github toolkit tools and use ToolFixer to fix their description.