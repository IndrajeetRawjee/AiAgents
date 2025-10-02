from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    function_args = function_call_part.args
    working_directory = "./calculator"
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    result = ""
    if function_name == "get_files_info":
        result =  get_files_info(working_directory,**function_args)
    if function_name == "get_file_content":
       result =  get_file_content(working_directory,**function_args)
    if function_name == "run_python_file":
        result =  run_python_file(working_directory,**function_args)
    if function_name == "write_file":
        result =  write_file(working_directory,**function_args)
    if result=="":
        return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"error": f"Unknown function: {function_name}"},
            )
        ],)
    else:
        return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": result},
            )
        ],
    
)