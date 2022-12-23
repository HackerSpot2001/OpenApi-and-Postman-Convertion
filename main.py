from yaml import safe_load,safe_dump
from json import load,dumps

def yamlToJson(yaml_filename,json_filename):
    try:
        with open(yaml_filename,"r") as f:
            data = safe_load(f)

        with open(json_filename,"w") as f:
            f.write(str(dumps(data)))
    except Exception as e:
        print("Error: ",str(e))
        exit(0)

def jsonToYaml(yaml_filename,json_filename):
    with open(json_filename,"r") as f:
        jsondata = load(f)
    
    with open(yaml_filename,"w") as f:
        f.write(str(safe_dump(jsondata)))


def startup():
    try:
        print("*"*100)
        print("\t\t\tWelcome to OpenAPI & Postman Collection Convertor.\t\t\t")
        print("*"*100)
        print("\nChoose option from given below:  ")
        print("\t1. OpenAPI to Postman.\n\t2. Postman to OpenAPI.\n\t3. Quit")
        mode = int(input("Enter Mode(ex:- 1,2 or 3): "))
        if (mode == 3):
            print("\tQuiting.....")
            exit(0)
            
        openApi = input("\tEnter OpenAPI File (ex:- eample.yaml): ")
        postman = input("\tEnter Postman File (ex:- eample.json): ")
        if (mode == 1):
            yamlToJson(openApi,postman)
        
        elif(mode == 2):
            jsonToYaml(openApi,postman)

        else:
            print("\nPlease Enter 1 or 2 with correct filename.")
            startup()
        
    except Exception as e:
        print("Error: ",str(e))
        exit(0)

if __name__ == "__main__":
    startup()