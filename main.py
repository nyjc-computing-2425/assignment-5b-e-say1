# Part 1
def read_csv(filename: str) -> list:
    '''
    reads the data from a csv file and edits it
    Parameters
    ----------
    filename: string
        name of file you want to edit
    '''
    enrolment_data = []
    # Type your code below
    with open(filename, "r") as f:
      header = f.readline().strip().split(",")
    
      for line in f:
          record = line.strip().split(",")
          record[0] = int(record[0])
          record[3] = int(record[3])
          enrolment_data.append(record)
        
    return header, enrolment_data


# Part 2
def filter_gender(enrolment_by_age: list, sex: str) -> list:
    """   
    filters and returns the data according to gender
    
    Parameters
    ----------
    enrolment_by_age: list
        name of list that you want to filter

    sex: string
        gender that you want to filter by

    Returns
    --------
    list
        a list that is filtered by the desired sex
    """
    # Type your code below
    new_list = []
    for rec in enrolment_by_age:
      if rec[2] == sex:
        new_list.append([rec[0], rec[1], rec[3]])
    
    return new_list


# Part 3
def sum_by_year(enrolment: list) -> list:
    '''
    sums up the enrolment by year

    Parameters
    ----------
    enrolment: list 
        name of list that you want to add up the sum for each year    
    '''
    yearly_data = []
    # Type your code below\
    year = enrolment[0][0]
    yearly_data = [[year, 0]]
    for metadata in enrolment:
        if year == metadata[0]:
          yearly_data[-1][-1] += metadata[-1]
        else:
          year = metadata[0]
          yearly_enrolment = metadata[-1]
          yearly_data.append([year, yearly_enrolment])

    return yearly_data  


# Part 4
def write_csv(filename: str, header: list, data: list) -> int:
    '''
    returns a file with the data written into it and an integer stating the number of lines written

    
    Parameters
    ----------
    filename: string
    name of file you want to write the data into 
    
    header: list
    header for the data in the file
    
    data: list
    list of data you want to write into the file 
    
    
    '''
    # Type your code below
    with open(filename, "w") as f:
      header = ["year", "total_enrolment"]
      header = ",".join(header) + "\n"
      f.write(header)
      length = len(data[0])
      line_number = 0
      for line in data:
        for i in range(length):
          line[i] = str(line[i])
        line = ",".join(line) + "\n"
        f.write(line)
        line_number += 1
    return line_number
  


# TESTING
# You can write code below to call the above functions
# and test the 
header, enrolment_data = read_csv("pre-u-enrolment-by-age.csv")
mf_enrolment = filter_gender(enrolment_data, "MF")
enrolment_by_year = sum_by_year(mf_enrolment)
write_csv("total-enrolment-by-year.csv", header, enrolment_by_year)







