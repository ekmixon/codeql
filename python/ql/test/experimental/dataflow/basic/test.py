def obfuscated_id(x): #$ step="FunctionExpr -> GSSA Variable obfuscated_id" step="x -> SSA variable x"
  return x

a = 42 #$ step="42 -> GSSA Variable a"
b = obfuscated_id(a) #$ flow="42, l:-1 -> GSSA Variable b" flow="FunctionExpr, l:-6 -> obfuscated_id" step="obfuscated_id(..) -> GSSA Variable b" step="GSSA Variable obfuscated_id, l:-6 -> obfuscated_id" step="GSSA Variable a, l:-1 -> a"
