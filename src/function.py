import io

def finfo(data):
    buffer = io.StringIO()
    data.info(buf=buffer)
    return buffer.getvalue()
            
def fdescribe(data):
    data = data.describe()
    return data
        
def fhead(data, n):
    data = data.head(n)
    return data
        
def fdropna(data):
    try:
        return data.dropna()
    except:
        return "Error!"
    
def ftail(data, n):
    data = data.tail(n)
    return data

def delete_row(data, n):
    try:
        return data.drop(n)
    except:
        return "Error!"
    
def select_column(data, n):
    try:
        return data.iloc[:, n]
    except:
        pass

def mean_column(data, n):
    column = select_column(data, n)
    try:
        mean = round((column).mean(), 2)
        return mean
    except:
        message = "Kesalahan! tidak dapat melakukan operasi, pastikan kolom ada dan tipe data kolom adalah integer atau float"
        return message

def median_column(data, n):
    column = select_column(data, n)
    try:
        median = round((column).median(), 2)
        return median
    except:
        message = "Kesalahan! tidak dapat melakukan operasi, pastikan kolom ada dan tipe data kolom adalah integer atau float"
        return message

def sum_column(data, n):
    column = select_column(data, n)
    try:
        if column.dtype.kind in 'ifu':
            summ = column.sum()
            return summ
        else:
            message = "Kesalahan! tidak dapat melakukan operasi, pastikan kolom ada dan tipe data kolom adalah integer atau float"
            return message
    except:
        message = "Kesalahan! tidak dapat melakukan operasi, pastikan kolom ada dan tipe data kolom adalah integer atau float"
        return message
    
def check_dtype(data, n):
    try:
        column_name = data.columns[n]
        name = column_name
        column = select_column(data, n)
        dtype = (column.dtype)
        return f"Tipe data kolom '{name}' (index {n}) adalah {dtype}"
    except:
        m = f"Kesalahan! tidak ada kolom dengan index ke-{n}"
        return m
    
def changer(type, input, n, data):
    input = input.split()
    n = int(n)
    column_name = data.columns[n]
    getdtypef =  data.iloc[:, n].dtype
    if type in input:   
        try:
            data[column_name] = data[column_name].astype(type)
            getdtypen = data[column_name].dtype
            return f"Mengubah kolom '{column_name}' (index {n}), dari {getdtypef} ke {getdtypen}"
        except Exception as e:
            return f"Terjadi kesalahan: {e}"

def change_type(user_input, n, data):
    targets = {
        "int": "int",
        "float": "float",
        "string": "string"
        }  
    try:
        for key, val in targets.items():
            if key in user_input:
                return changer(val, user_input, n, data)

    except:
        return f"Terjadi kesalahan!"
        

def fill(data, n, user_input):
    method_list = {"mean": "mean", "median": "median"}
    keyword = ["semua", "seluruh", "semuanya"]
    user_input = user_input.split()
    method = next((val for key, val in method_list.items() if key in user_input), None)

    try:
        if any(k in user_input for k in keyword):
            fill_values = getattr(data, method)(numeric_only=True)
            data.fillna(fill_values, inplace=True)
            return data
        else:
            column_name = data.columns[n]
            fill_value = getattr(data[column_name], method)()
            data[column_name] = data[column_name].fillna(fill_value)
            return data[column_name]
            
    except Exception as e:
        return f"Terjadi kesalahan: {e}"


    
