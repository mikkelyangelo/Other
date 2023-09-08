#include <math.h>
#include <vector>
#include <string>
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
void zero(Matrix& m) {
 for (int i = 0; i < m.size(); ++i) {
 std::fill(m[i].begin(), m[i].end(), 0);
 }
}
void print(const Matrix& m) {
 for (int i = 0; i < m.size(); ++i) {
 for (int j = 0; j < m[i].size(); ++j) {
 printf("%-20.8f ", m[i][j]);
 }
 puts("");
 }
}
Vector create_vector(int size) {
 Vector res;
 res.resize(size, 0);
 return res;
}
void zero(Vector& v) {
 std::fill(v.begin(), v.end(), 0);
}
void print(const Vector& v) {
 for (int i = 0; i < v.size(); ++i) {
 printf("%5f ", v[i]);

 }
 puts("");
}
// it breaks contents of m and b
int gauss(Matrix& m, Vector& b) {
 for (int k = 0; k < m.size(); ++k) {
 if (fabs(m[k][k]) < 1e-17) {
 return 1;
 }
 double diagonal = m[k][k];
 // divide this row by diagonal element
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
Vector solve_FEM(const Matrix& local_matrix, const Vector&
local_vector, int n) {
 // assemble matrix
 auto matrix = create_matrix(n+1, n+1);
 for (int i = 0; i < n; ++i) {
 matrix[i][i] += local_matrix[0][0];
 matrix[i][i+1] += local_matrix[0][1];
 matrix[i+1][i] += local_matrix[1][0];
 matrix[i+1][i+1] += local_matrix[1][1];
 }
 // assemble vector
 auto vector = create_vector(n+1);
 for (int i = 0; i < n; ++i) {
 vector[i] += local_vector[0];
 vector[i+1] += local_vector[1];
 }
 // assign known variables
 vector[0] = 10;
 matrix[0][0] = 1;
 matrix[0][1] = 0;
 vector[n] = 1;