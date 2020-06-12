#include "randoms.hh"

static std::random_device rd;
static const int seed = 1137; //constant seed for debug purposes
// static std::mt19937 twister{rd()};
static std::mt19937 twister{seed};

//return an integer number between @left and @right
int rand_int(int left, int right)
{
    std::uniform_int_distribution<int> int_dist(left, right);
    auto r_int = int_dist(twister);
    return r_int;
}

//returns a vector with @CT_SIZE which contains random integers between @left and @right
std::vector<int> generate_random_container(size_t ct_size, int left, int right)
{
    std::vector<int> rand_ctr;
    for (auto id = 0; id < ct_size; ++id)
    {
        auto current_rand = rand_int(left, right);
        rand_ctr.emplace_back(current_rand);
    }
    return rand_ctr;
}

template <typename T>
double average(const std::vector<T> &v)
{
    double sum = 0.0;
    for (auto &&elem : v)
    {
        sum = sum + elem;
    }
    return static_cast<double>(sum / v.size());
}

PyObject *generate_randoms(PyObject *self, PyObject *args)
{
    Py_ssize_t arr_size;
    int left, right;
    if (!PyArg_ParseTuple(args, "nii", &arr_size, &left, &right))
        return NULL;
    auto cxx_container = generate_random_container(arr_size, left, right);
    PyObject *result;
    PyObject *py_container = PyList_New(arr_size);
    for (auto id = 0; id < arr_size; ++id)
    {
        PyObject *current_int = PyLong_FromLong(cxx_container.at(id));
        PyList_SetItem(py_container, id, current_int);
    }
    auto avg = average(cxx_container);
    result = Py_BuildValue("Od", py_container,avg);
    Py_XDECREF(py_container);
    return result;
}