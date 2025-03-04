# Custom tools

This is a collection of custom developed tools, which are created with the intention of testing our method **ToolFuzz**.
Most of these tool have insufficiencies in their documentation which allow for models to invoke the tools with
parameters which result in AssertionErrors.

We have developed two tools for correctness testing, these tools lack specification of their
parameters - [open_street_map_search, open_street_map_distance](./open_street_map.py)