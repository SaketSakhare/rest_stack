from fastapi import FastAPI
from stack import stack
from exceptions import NegativeStack, StackEmpty, StackFull
from fastapi.responses import JSONResponse

app = FastAPI()
stack_obj = None


@app.post('/initialize/{size}')
def initilize(size):
    size = int(size)
    # import pdb; pdb.set_trace()
    if size < 1:
        return JSONResponse({"Response": "Stack size should be more than 0",}, status_code=403)
    global stack_obj
    stack_obj = stack(size)
    return JSONResponse({"Response": "Stack initialized"}, status_code=201)




@app.post('/push/{integer}')
def push(integer):
    integer = int(integer)
    if stack_obj is None:
        return JSONResponse({"Response": "initialize the stack first using /initialize/<size>"}, status_code=400)
    try:
        stack_obj.push(integer=integer)
        return JSONResponse({"Response": "Pushed to stack", "element":  integer}, status_code=201)
    except StackFull as e:
        print(str(e))
        return JSONResponse({"Response": "Stack is Full"}, status_code=507)
    except Exception as e:
        print(str(e))
        return JSONResponse({"Response": "Unknown Error"}, status_code=500)


@app.delete('/pop')
def pop():
    if stack_obj is None:
        return JSONResponse({"Response": "initialize the stack first using /initialize/<size>"}, status_code=400)
    try:
        delete_element = stack_obj.pop()
        return JSONResponse({"Response": "Poped from stack", "element":  delete_element}, status_code=200)
    except StackEmpty as e:
        print(str(e))
        return JSONResponse({"Response": "Stack is Empty"}, status_code=404)
    except Exception as e:
        print(str(e))
        return JSONResponse({"Response": "Unknown Error"}, status_code=500)


@app.get("/peak")
def peak():
    if stack_obj is None:
        return JSONResponse({"Response": "initialize the stack first using /initialize/<size>"}, status_code=400)
    try:
        top_element =  stack_obj.peak()
        if top_element:
            return JSONResponse({"Response": "Peaked from stack", "element":  top_element}, status_code=200)
        else:
            return JSONResponse({"Response": "Empty stack, nothing to peak",}, status_code=200)
    except NegativeStack as e:
        print(str(e))
        return JSONResponse({"Response": "Stack initialized using negative number"}, status_code=404)
    except Exception as e:
        print(str(e))
        return JSONResponse({"Response": "Unknown Error"}, status_code=500)
