def execute_python(code, df=None):
    local_vars = {"df": df}

    try:
        exec(code, {}, local_vars)
        return local_vars.get("result", df)
    except Exception as e:
        return f"ERROR: {str(e)}"
