# Imports and variable initializations
import numpy as np
import random as rd
rd.seed(10)
stored_matrices = []

# An matrix class to store numpy particulars
class Matrix:
    def __init__(self, row=1, column=1):
        self.row = row
        self.column = column
        self.matrix = np.zeros((row,column), dtype=float)
    # Re-populate matrix with random int variable
    def randomRepopulation(self):
        for r in range(self.row):
            for c in range(self.column):
                self.matrix[r,c] = rd.randint(0, 10)
    # Re-populate matrix with user's inputs of int variables
    def manualRepopulation(self):
        for r in range(self.row):
            print('Row',r+1)
            for c in range(self.column):
                print('Column',c+1,'(enter):',end='')
                self.matrix[r,c] = int(input())
# Add each element of all matrices (as long as each matrix's shape match)
def addition():
    sum_total_m = stored_matrices.pop()
    while (len(stored_matrices)>0):
        temp_m = stored_matrices.pop()
        try:
            sum_total_m.matrix = np.add(sum_total_m.matrix,temp_m.matrix)
        except ValueError:
            print('Matrices do not match:',sum_total_m.matrix.shape,'!=',temp_m.matrix.shape)
            break
    # Return the total sum of all matrices
    return sum_total_m
# Take the average of the matrices
def average():
    # Get the total sum of all matrices
    total_m = float(len(stored_matrices))
    avg_total_m = addition()
    # Average every element in the matrix
    for r in range(avg_total_m.row):
        for c in range(avg_total_m.column):
            avg_total_m.matrix[r, c] = avg_total_m.matrix[r, c] / total_m
    # Return the total average of all matrices
    return avg_total_m

if __name__ == '__main__':
    #Create matrices
    matrices = int(input('Matrices to create:'))

    for matrix in range(matrices):
        print('\nMatrix',matrix+1)
        row = int(input('Enter matrix row:'))
        column = int(input('Enter matrix column:'))
        m = Matrix(row, column)
        #Prompt user for matrix repopulation options
        if input('Randomly repopulate matrix(y,n):')=='y': m.randomRepopulation()
        elif input('Manually repopulate matrix(y,n):')=='y': m.manualRepopulation()
        else: print('Creating matrix with zeros...')
        #Store matrix
        stored_matrices.append(m)

    #Matrix calculations
    #print('\nNewly added matrix:\n',addition())
    print('\nNewly averaged matrix:\n',average().matrix)