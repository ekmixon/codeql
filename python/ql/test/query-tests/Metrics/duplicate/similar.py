

def original(the_ast):
    def walk(node, in_function, in_name_main):
        def flags():
            return in_function * 2 + in_name_main

        if isinstance(node, ast.Module):
            yield from walk(node.body, in_function, in_name_main)
        elif isinstance(node, ast.ImportFrom):
            aliases = [ Alias(a.name, a.asname) for a in node.names]
            yield FromImport(node.level, node.module, aliases, flags())
        elif isinstance(node, ast.Import):
            aliases = [ Alias(a.name, a.asname) for a in node.names]
            yield Import(aliases, flags())
        elif isinstance(node, ast.FunctionDef):
            for _, child in ast.iter_fields(node):
                yield from walk(child, True, in_name_main)
        elif isinstance(node, list):
            for n in node:
                yield from walk(n, in_function, in_name_main)

    return list(walk(the_ast, False, False))

def similar_1(the_ast):
    def walk(node, in_function, in_name_main):
        def flags():
            return in_function * 2 + in_name_main

        if isinstance(node, ast.Module):
            yield from walk(node.body, in_function, in_name_main)
        elif isinstance(node, ast.ImportFrom):
            aliases = [ Alias(a.name, a.asname) for a in node.names]
            yield FromImport(node.level, node.module, aliases, flags())
        elif isinstance(node, ast.Import):
            aliases = [ Alias(a.name, a.asname) for a in node.names]
            yield Import(aliases, flags())
        elif isinstance(node, ast.FunctionDef):
            for _, child in ast.iter_fields(node):
                yield from walk(child, True, in_name_main)

    return list(walk(the_ast, False, False))

def similar_2(the_ast):
    def walk(node, in_function, in_name_main):
        def flags():
            return in_function * 2 + in_name_main

        if isinstance(node, ast.Module):
            yield from walk(node.body, in_function, in_name_main)
        elif isinstance(node, ast.Import):
            aliases = [ Alias(a.name, a.asname) for a in node.names]
            yield Import(aliases, flags())
        elif isinstance(node, ast.FunctionDef):
            for _, child in ast.iter_fields(node):
                yield from walk(child, True, in_name_main)
        elif isinstance(node, list):
            for n in node:
                yield from walk(n, in_function, in_name_main)

    return list(walk(the_ast, False, False))
