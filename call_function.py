from google.genai import types

def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    function_args = function_call_part.args