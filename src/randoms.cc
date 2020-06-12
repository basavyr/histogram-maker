#include "randoms.hh"

 PyObject *generate_randoms(PyObject *self, PyObject *args)
{
    Py_ssize_t arr_size;
    int left, right;
    if (!PyArg_ParseTuple(args, "nii", &arr_size, &left, &right))
        return NULL;
    PyObject *result;
    std::string name = "Build Works OK";
    result = Py_BuildValue("s", name.c_str());
    return result;
}