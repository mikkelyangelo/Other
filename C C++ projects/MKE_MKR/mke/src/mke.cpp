#include <math.h>
#include <vector>
#include <string>
#include <cassert>

typedef std::vector<std::vector<double>> Matrix;
typedef std::vector<double> Vector;

Matrix create_matrix(int rows, int cols) {
    Matrix res;
    res.resize(rows);
    for (int i = 0; i < rows; ++i) {
        res[i].resize(cols, 0);
    }
    return res;
}

Vector create_vector(int size) {
    Vector res;
    res.resize(size, 0);
    return res;
}

int gauss(Matrix& m, Vector& b) {
    for (int k = 0; k < m.size(); ++k) {
        if (fabs(m[k][k]) < 1e-17) {
            return 1;
        }
        double diagonal = m[k][k];
        for (int i = k; i < m.size(); ++i) {
            m[k][i] /= diagonal;
        }
        b[k] /= diagonal;

        for (int i = k+1; i < m.size(); ++i) {
            double elem = m[i][k];
            for (int j = k; j < m.size(); ++j) {
                m[i][j] -= elem * m[k][j];
            }
            b[i] -= elem * b[k];
        }
    }
    for (int i = m.size()-2; i >= 0; --i) {
        for (int j = i + 1; j < m.size(); ++j) {
            b[i] -= m[i][j] * b[j];
        }
    }
    return 0;
}

Vector solve(const Matrix& local_matrix, const Vector& local_vector, int n) {
    auto matrix = create_matrix(n+1, n+1);
    for (int i = 0; i < n; ++i) {
        matrix[i][i] += local_matrix[0][0];
        matrix[i][i+1] += local_matrix[0][1];
        matrix[i+1][i] += local_matrix[1][0];
        matrix[i+1][i+1] += local_matrix[1][1];
    }

    auto vector = create_vector(n+1);
    for (int i = 0; i < n; ++i) {
        vector[i] += local_vector[0];
        vector[i+1] += local_vector[1];
    }
    vector[0] = 10;
    matrix[0][0] = 1;
    matrix[0][1] = 0;
    vector[n] = 1;
    matrix[n][n] = 1;
    matrix[n][n - 1] = 0;

    if (gauss(matrix, vector) != 0) {
        puts("Error: degraded matrix");
        exit(-1);
    }
    return vector;
}

void save(const Vector& vector, const std::string& name) {
    FILE *f = fopen(name.c_str(), "w");
    assert(f);
    double L = 7.0 / (vector.size() - 1);
    for (int i = 0; i < vector.size(); ++i) {
        fprintf(f, "%lf %lf\n", -1.0 + i * L, vector[i]);
    }
    fclose(f);
}

void compress(Matrix& matrix, Vector& vector) {
    for (int i = 1; i < 3; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (fabs(matrix[j][i]) < 1e-10 || i == j) {
                continue;
            }
            double val = matrix[j][i]/matrix[i][i];
            vector[j] -= val * vector[i];
            for (int k = 0; k < 4; ++k) {
                matrix[j][k] -= val * matrix[i][k];
            }
        }
    }
}

double max_different(const Vector& a, const Vector& b) {
    double max_dif = a[0] - b[0];
    for (int i = 1; i < a.size(); ++i) {
        auto d = fabs(a[i] - b[i]);
        if (d > max_dif) {
            max_dif = d;
        }
    }
    return max_dif;
}

Vector analytical(int node_count) {
    Vector result;
    result.resize(node_count);
   double l = 7.0 / (node_count - 1);
    for (int i = 0; i < node_count; ++i) {
        double x = l * i;
   //double q = 0.0000001;
        result[i] = (exp(14./5) * (33. - 5 * x) - 53 * exp(-2. / 5 * (x - 7.)) + 5. * (x + 4)) / (2. - 2 * exp(14./5));
    }
    return result;
  //  double t = exp(14.0 / 5.0);
     //   double L = 7.0 / (node_count - 1);
     //   for (int i = 0; i < node_count; ++i) {
      //          double x = L * i;
       //         double a = (20.0 + 33.0 * t) / (2.0 - 2.0 * t);
      //          double b = 53.0 * t / (2.0 * t - 2.0);
      //         result[i] = a + b * exp(-0.4 * x) + 2.5 * x; 
      //  }
      //  return result;
}

Vector linear(int node_count) {
    double L = 7.0 / (node_count-1);
    Matrix local_matrix = {
            { 
            	-1 - 5 / L, 1 + 5 / L
            },
            { 
            -1 + 5 / L,
                        1 - 5 / L
            },
    };
    Vector local_vector = {
            5. * L / 2.,
            5. * L / 2.
    };
    return solve(local_matrix, local_vector, node_count - 1);
}

Vector cubic(int node_count) {
    double L = 7.0 / (node_count-1);
	Matrix temp_matrix = {
                {
                        -37.0 / (2 * L) - 1.0, 189.0 / (8 * L) + 57.0 / 40, -27.0 / (4 * L) - 3.0 / 5, 13.0 / (8 * L) + 7.0 / 40
                },
                {
                        189.0000001 / (8 * L) - 57.0 / 40,
                        -54.0 / L,
                        297.0 / (8 * L) + 81.0 / 40,
                        -27.0 / (4 * L) - 3.0 / 5
                },
                {
                        -27.0 / (4 * L) + 3.0 / 5,
                        297.0 / (8 * L) - 81.0 / 40,
                        -54.0 / L,
                        189 / (8 * L) + 57.0 / 40
                },
                {
                        13.0 / (8 * L) - 7.0 / 40,
                        -27.0 / (4 * L) + 3.0 / 5,
                        189.0 / (8 * L) - 57.0 / 40,
                        -37.0 / (2 * L) + 1
                }
        };
    Vector temp_vector = {
            5. * L / 8.0,
            5. * 3.0 * L / 8.0,
            5. * 3.0 * L / 8.0,
            5. * L / 8.0,
    };
    compress(temp_matrix, temp_vector);
    Matrix local_matrix = {
            {temp_matrix[0][0], temp_matrix[0][3]},
            {temp_matrix[3][0], temp_matrix[3][3]}
    };
    Vector local_vector = {
            temp_vector[0],
            temp_vector[3]
    };
    return solve(local_matrix, local_vector, node_count - 1);
}

int main() {
    int node_count_1 = 20;
    int node_count_2 = 40;

    auto analytic20 = analytical(node_count_1);
    save(analytic20, "analytic20.txt");

    auto analytic40 = analytical(node_count_2);
    save(analytic40, "analytic40.txt");

    auto linear20 = linear(node_count_1);
    save(linear20, "linear20.txt");

    auto linear40 = linear(node_count_2);
    save(linear40, "linear40.txt");

    auto cubic20 = cubic(node_count_1);
    save(cubic20, "cubic20.txt");

    auto cubic40 = cubic(node_count_2);
    save(cubic40, "cubic40.txt");

    printf("analytic20/linear20/cubic20/error_linear20/error_cubic20\n");
    for (int i = 0; i < analytic20.size(); ++i) {
        printf("%g ", analytic20[i]);
        printf("%g ", linear20[i]);
        printf("%g ", cubic20[i]);
        printf("%g ",(double)  (analytic20[i] - linear20[i]));
        printf("%g\n", analytic20[i] - cubic20[i]);
    }

    printf("\nanalytic40/linear40/cubic40/error_linear40/error_cubic40\n");
    for (int i = 0; i < analytic40.size(); ++i) {
        printf("%g ", analytic40[i]);
        printf("%g ", linear40[i]);
        printf("%g ", cubic40[i]);
        printf("%g ", analytic40[i] - linear40[i]);
        printf("%g\n", analytic40[i] - cubic40[i]);
    }
    printf("\n");

    int node_count = 6000;
    auto linearn = linear(node_count);
    save(linearn, "linearn.txt");
    auto analyticn = analytical(node_count);
    save(analyticn, "linearn.txt");
    printf("Error linear (%d nodes): %g\n", node_count, max_different(analyticn, linearn));
    printf("Error cubic (20 nodes): %g\n", max_different(analytic20, cubic20));
    return 0;
}
