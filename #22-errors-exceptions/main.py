# try-except
try:
    10 / 0
except ZeroDivisionError:
    print(dir(ZeroDivisionError))
    print('Division by zero')
except:
    print("hello")

print('Continue...')


# get error info
try:
    10 / 'j'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

print("Continue ...")


# else finally blocks
try:
    ...
except TypeError:
    ...
except:
    ...
else:
    print("No erors")
finally:
    print("All are come (maybe was errors maybe not)")


# if absent type of Error
print('\n')
try:
    10 / 4
except Exception as e:
    print(e)
else:
    print('All right!')
finally:
    print('All over')


# generete self-created errors with 'rise'

def div(a, b):
    if b == 0:
        raise TypeError("Error: second argument can't be 0")
    return a / b


try:
    div(10, 0)
except Exception as e:
    print(e)

# Home Task
print("\n\n")


def generate_error(param, err_no):
    return f"[Error-{err_no}]: missimg key '{param}' in container"


def image_info(container: dict):
    if not 'image_id' in container:
        raise TypeError(generate_error('image_id', 23))
    if not 'image_title' in container:
        raise TypeError(generate_error('image_title', 45))
    return f"Image '{container['image_title']}' has id {container['image_id']}'"


cat_dict = {
    'image_id': 4500,
    'image_title': "My little cat"
}

img_inf = ''
try:
    img_inf = image_info(cat_dict)
except Exception as ex:
    print(ex)
else:
    print("Success...\n", img_inf)
finally:
    print("Program finished.")
