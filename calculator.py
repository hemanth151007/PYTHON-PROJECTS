def parsing_input():
    expression=input("enter your expression for calculation:")
    try:
        a,op,b=expression.split()
        return float(a),op,float(b)
    except ValueError:
        print("error occured")
    return None,None,None
def calculation(a,op,b):
    operations={
        "+":lambda a,b : a+b,
        "-":lambda a,b : a-b,
        "*":lambda a,b : a*b,
        "/":lambda a,b : a/b if b!=0 else "zero division error",
        "%":lambda a,b : a%b if b!=0 else "error"
    }
    if op in operations:
        result=operations[op](a,b)
    return result

def main():
    history=[]
    a,op,b=parsing_input()
    result=calculation(a,op,b)
    history.append(f"{a} {op} {b} = {result}")
    print("result:", result)
    
    while True:
        expr=input("enter your expression for calculation like (op b) or type 'history' to view history or 'clear' to clear history:")
        if expr.lower()=="history":
            print("calculation history:",history)
            continue
        elif expr.lower()=="clear":
            history.clear()
            print("history clered")
            continue
        elif expr.lower()=="exit":
            print("thank you for using the calculator!")
            break
        #parsing input 
        try:
            op,b=expr.split()
            b=float(b)
        except ValueError:
            print("invalid input")
            continue
        a=result
        result=calculation(a,op,b)
        history.append(f"{a} {op} {b} = {result}")
        print("result:", result)


if __name__=="__main__":
    main()
