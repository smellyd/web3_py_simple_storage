from solcx import compile_standard

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    # read from the SimpleStorage.sol file and place it in the variable
    # print(simple_storage_file)

    #Compile our Solidity

compiled_sol = compile_standard(
    {
        'language':'Solidity',
        'sources':{'SimpleStorage.sol': {'content': simple_storage_file}},
        'settings': {
            'outputSelection': {
                '*' : {'*': ['abi', 'metadata', 'evm.bytecode', 'evm.sourceMap']}
                }
            },
        },
        solc_version='0.6.0',
    )
print(compiled_sol)
 