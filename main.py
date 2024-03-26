# Part 1
enrolment_data = []
filter = []
yearly_data = []
def read_csv(filename: str) -> list:
  '''
  filename: Name of file (string)
  
  returns a nested list of data in the file
  '''
    # Type your code below
  with open(filename, "r") as f:
      header = f.readline().strip().split(",")
  
      for line in f:
        metadata = line.strip().split(",")
        metadata[0] = int(metadata[0])
        metadata[3] = int(metadata[3])
        enrolment_data.append(metadata)
        
  return header, enrolment_data
  pass


# Part 2
def filter_gender(enrolment_by_age: list, sex: str) -> list:
  '''
  enrolment_by_age: name of list that you want to filter (variable name)
  
  sex: gender that you want to filter by (string)

  returns a list that is filtered by the desired sex
  '''
    # Type your code below
  for metadata in enrolment_by_age:
      if metadata[2] == sex:
        filter.append(metadata)
        metadata.pop(2)
    

  return filter
  pass


# Part 3
def sum_by_year(enrolment: list) -> list:
  '''
  enrolment: name of list that you want to add up the sum for each year (variable name)

  returns a list that contains all the years and their respective enrolment numbers
  
  '''
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
  pass


# Part 4
def write_csv(filename: str, header: list, data: list) -> int:
  '''
  filename: name of file you want to write the data into (string, including extension)
  
  header: header for the data in the file (variable name)
  
  data: list of data you want to write into the file (variable name)

  returns a file with the data written into it and an integer stating the number of lines written

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
      print(line_number)
  return line_number
  pass


# TESTING
# You can write code below to call the above functions
# and test the 
header, file = read_csv("pre-u-enrolment-by-age.csv")
mf_enrolment = filter_gender(enrolment_data, "MF")
enrolment_by_year = sum_by_year(mf_enrolment)
write_csv("total-enrolment-by-year.csv", header, enrolment_by_year)







