from ..models import Variable

def get_variables():
    variables = Variable.objects.all()
    return variables

def get_variable(var_pk):
    variable = Variable.objects.get(pk=var_pk)
    return variable

def update_variable(var_pk, new_var):
    variable = get_variable(var_pk)
    variable.name = new_var["name"]
    variable.save()
    return variable

def create_variable(var):
    variable = Variable(name=var["name"])
    variable.save()
    return variable
