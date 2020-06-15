#include "randoms.hh"

static std::random_device rd;
static const int seed = 1137; //constant seed for debug purposes
// static std::mt19937 twister{rd()};
static std::mt19937 twister{seed};

template <typename T>
struct Counter
{
    T counters;
    T elements;
};

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

template <typename vType, typename argType>
std::vector<vType> normal_dist_container(size_t size, argType mean, argType std_dev)
{
    std::vector<vType> data;

    //the norma distribution must be float or double
    //the integer container will be generated through the round function
    std::normal_distribution<double> normal(static_cast<double>(mean), static_cast<double>(std_dev));

    for (auto id = 0; id < size; ++id)
    {
        auto current_normal = std::round(normal(twister));
        data.emplace_back(static_cast<vType>(current_normal));
    }
    return data;
}

template <typename T>
std::vector<T> minmax_normalize(const std::vector<T> &v)
{
    std::vector<T> normalized_v;
    auto extrems = std::minmax_element(v.begin(), v.end());
    T minval = *extrems.first;
    T maxval = *extrems.second;
    for (auto id = 0; id < v.size(); ++id)
    {
        //get the nearest integer
        auto current_value = std::round((v.at(id) - minval) / (maxval - minval));
        normalized_v.emplace_back(current_value);
    }
    return normalized_v;
}

std::vector<Counter<int>> count_data(std::vector<int> v)
{
    std::sort(v.begin(), v.end());
    std::vector<Counter<int>> counted_elements;
    int count = 0;
    counted_elements.emplace_back();
    counted_elements.at(count).elements = v.at(count);
    counted_elements.at(count).counters++;
    for (int id = 1; id < v.size(); ++id)
    {
        auto current_element = v.at(id);
        if (counted_elements.at(count).elements != current_element)
        {
            count++;
            counted_elements.emplace_back();
            counted_elements.at(count).elements = v.at(id);
            ++counted_elements.at(count).counters;
        }
        else
        {
            ++counted_elements.at(count).counters;
        }
    }
    return counted_elements;
}

std::pair<int, int> frequency(const std::vector<Counter<int>> &v, int which)
{
    std::pair<int, int> P;
    P.first = which;
    P.second = 0;
    for (auto id = 0; id < v.size(); ++id)
    {
        if (P.first == v.at(id).elements)
        {
            P.second = v.at(id).counters;
        }
    }
    return P;
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
    result = Py_BuildValue("Od", py_container, avg);
    Py_XDECREF(py_container);
    return result;
}

PyObject *generate_normalDistribution(PyObject *self, PyObject *args)
{
    Py_ssize_t data_size;
    double mean, std_dev;
    if (!PyArg_ParseTuple(args, "ndd", &data_size, &mean, &std_dev))
        return NULL;
    PyObject *result;
    auto data = normal_dist_container<int, double>(data_size, mean, std_dev);
    PyObject *py_data = PyList_New(data_size);
    for (auto id = 0; id < data_size; ++id)
    {
        auto current_element = data.at(id);
        PyObject *element_pure = PyLong_FromLong(current_element);
        PyList_SetItem(py_data, id, element_pure);
    }
    result = Py_BuildValue("O", py_data);
    Py_XDECREF(py_data);
    return result;
}

PyObject *generate_clHistogram(PyObject *self, PyObject *args)
{
    Py_ssize_t arr_size;
    double mean, std_dev;
    if (!PyArg_ParseTuple(args, "ndd", &arr_size, &mean, &std_dev))
        return NULL;
    auto data = normal_dist_container<int, double>(arr_size, mean, std_dev);
    std::sort(data.begin(), data.end());
    PyObject *result;
    PyObject *py_data = PyList_New(arr_size);
    for (auto id = 0; id < arr_size; ++id)
    {
        auto current_element = data.at(id);
        PyObject *element_pure = PyLong_FromLong(current_element);
        PyList_SetItem(py_data, id, element_pure);
    }
    result = Py_BuildValue("O", py_data);
    Py_XDECREF(py_data);
    return result;
}