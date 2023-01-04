def gearbox (gear):
    if gear.lower() == 'manual':
        return [1]
    elif gear.lower() == "auto":
        return [0]



def vehicle_Type (vtype):
    if vtype.lower() == 'bus':
        return [1,0,0,0,0,0,0]
    elif vtype.lower() == 'cabrio':
        return [0,1,0,0,0,0,0]
    elif vtype.lower() == 'coupe':
        return [0,0,1,0,0,0,0]
    elif vtype.lower() == 'kleinwagen':
        return [0,0,0,1,0,0,0]
    elif vtype.lower() == 'limousine':
        return [0,0,0,0,1,0,0]
    elif vtype.lower()  == 'suv':
        return [0,0,0,0,0,1,0]
    elif vtype.lower() == 'van':
        return [0,0,0,0,0,0,1]


def car_model (model):
    if model.lower() == 'beetle':
        return [1,0,0,0,0,0,0]
    elif model.lower() == 'golf':
        return [0,1,0,0,0,0,0]
    elif model.lower() == 'passat':
        return [0,0,1,0,0,0,0]
    elif model.lower() == 'polo':
        return [0,0,0,1,0,0,0]
    elif model.lower() == 'scirocco':
        return [0,0,0,0,1,0,0]
    elif model.lower() == 'tiguan':
        return [0,0,0,0,0,1,0]
    elif model.lower() == 'touran':
        return [0,0,0,0,0,0,1]      



def fuel_Type (ftype):
    if ftype.lower() == 'diesel':
        return [1,0,0,0]
    elif ftype.lower() == 'electric':
        return [0,1,0,0]
    elif ftype.lower() == 'gasoline':
        return [0,0,1,0]
    elif ftype.lower() == 'hybrid':
        return [0,0,0,1]


def get_preprocess (data):
    year= data['year']
    gear= gearbox(data['gearbox'])
    powerPS= data['powerh']
    kilometer= data['kilometer']
    vehicleType= vehicle_Type(data['cartype'])
    model= car_model(data['model'])
    fueltype= fuel_Type(data['fueltype'])
    final_data= [ year , powerPS ,  kilometer ]  + gear + vehicleType + model + fueltype
    return final_data   