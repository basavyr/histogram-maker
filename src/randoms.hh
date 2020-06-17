#include "Python.h"

#include <iostream>
#include <random>
#include <string>
#include <chrono>
#include <map>
#include <cmath>
#include <algorithm>

#if PY_MAJOR_VERSION >= 3
#define PY3K
#endif

static const char ModuleDoc[] = "This is an extension that generates random numbers using the Mersenne Twister from the STL";
static const char ModuleName[] = "randoms";

PyObject *generate_randoms(PyObject *self, PyObject *args);
static const char generate_randomsMethodName[] = "randoms";
static const char generate_randomsMethodDoc[] = "This method returns a container with N random elements inside. N is aribtrary - set by user";

PyObject *generate_normalDistribution(PyObject *self, PyObject *args);
static const char generate_normalDistributionMethodName[] = "distribution";
static const char generate_normalDistributionMethodDoc[] = "This method returns a container that has a normal distributed data set.";

PyObject *generate_clHistogram(PyObject *self, PyObject *args);
static const char generate_clHistogramMethodName[] = "clhistogram";
static const char generate_clHistogramMethodDoc[] = "This method returns a visual histogram, when executed by the user from the command line. Uses std::map from C++";

PyObject *showSeeds(PyObject *self);
constexpr char showSeedsMethodName[] = "seeds";
constexpr char showSeedsMethodDoc[] = "This method returns the random device seed and the Mersenne seed that are used for the container generation";

static PyMethodDef randomsMethodDef[] = {
    {generate_randomsMethodName, generate_randoms, METH_VARARGS, generate_randomsMethodDoc},
    {generate_normalDistributionMethodName, generate_normalDistribution, METH_VARARGS, generate_normalDistributionMethodDoc},
    {generate_clHistogramMethodName, generate_clHistogram, METH_VARARGS, generate_clHistogramMethodDoc},
    {showSeedsMethodName, (PyCFunction)showSeeds,METH_NOARGS, showSeedsMethodDoc},
    {NULL, NULL, 0, NULL}};

#ifdef PY3K
static struct PyModuleDef randomsModuleDef = {
    PyModuleDef_HEAD_INIT,
    ModuleName,
    ModuleDoc,
    -1,
    randomsMethodDef};

PyMODINIT_FUNC PyInit_randoms(void)
{
    Py_Initialize();
    PyObject *m;
    m = PyModule_Create(&randomsModuleDef);
    return m;
}
#else
PyMODINIT_FUNC initrandoms(void)
{
    Py_InitModule3(ModuleName, randomsMethodDef, ModuleDoc);
}
#endif