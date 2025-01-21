# Name: Lisette Ruano
# Class: CS 341, Fall 2024
# Overview: Chicago Lobbyist Database App
#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through 
# the data tier.
#
# Original author: Ellen Kidane
#
import datatier


##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
class Lobbyist:
   def __init__(self, id, firstName, lastName, phone):
      self._Lobbyist_ID = id
      self._First_Name = firstName
      self._Last_Name = lastName
      self._Phone = phone

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Phone(self):
      return self._Phone

##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:
   def __init__(self, id, salutation, firstName, midIntial, lastName, suffix, address1, address2, city, state, zip, country, email, phone,fax, yearsReg, employers, totCompensation):
      self._Lobbyist_ID = id
      self._Salutation = salutation
      self._First_Name = firstName
      self._Middle_Initial = midIntial
      self._Last_Name = lastName
      self._Suffix = suffix
      self._Address_1 = address1
      self._Address_2 = address2
      self._City = city
      self._State_Inital = state
      self._Zip_Code = zip
      self._Country = country
      self._Email = email
      self._Phone = phone
      self._Fax = fax
      self._Years_Registered = yearsReg
      self._Employers = employers
      self._Total_Compensation = totCompensation

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID
        
   @property
   def Salutation(self):
      return self._Salutation

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Middle_Initial(self):
      return self._Middle_Initial

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Suffix(self):
      return self._Suffix

   @property
   def Address_1(self):
      return self._Address_1

   @property
   def Address_2(self):
      return self._Address_2

   @property
   def City(self):
      return self._City

   @property
   def State_Initial(self):
      return self._State_Inital

   @property
   def Zip_Code(self):
      return self._Zip_Code

   @property
   def Country(self):
      return self._Country

   @property
   def Email(self):
      return self._Email

   @property
   def Phone(self):
      return self._Phone

   @property
   def Fax(self):
      return self._Fax

   @property
   def Years_Registered(self):
      return self._Years_Registered

   @property
   def Employers(self):
      return self._Employers

   @property
   def Total_Compensation(self):
      return self._Total_Compensation

##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:
   def __init__(self, id, firstName, lastName, phone, totCompensation, clients):
      self._Lobbyist_ID = id
      self._First_Name = firstName
      self._Last_Name = lastName
      self._Phone = phone
      self._Total_Compensation = totCompensation
      self._Clients = clients

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Phone(self):
      return self._Phone

   @property
   def Total_Compensation(self):
      return self._Total_Compensation

   @property
   def Clients(self):
      return self._Clients


##################################################################
# 
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
   sql = """ select count(Lobbyist_ID) from LobbyistInfo """

   try:
      single = datatier.select_one_row(dbConn, sql)
      totalLobbyists = single[0]
      return totalLobbyists
   except Exception as err:
        return -1
   
   

##################################################################
# 
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):

   sql = """select count(Employer_ID) from EmployerInfo """

   try:
      single = datatier.select_one_row(dbConn, sql)
      totalEmployers = single[0]
      return totalEmployers
   except Exception as err:
        return -1

   


##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
   sql = """select count(Client_ID) from ClientInfo """

   try:
      single = datatier.select_one_row(dbConn, sql)
      totalClients = single[0]
      return totalClients
   except Exception as err:
        return -1

##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and % 
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):
   sql = """ select Lobbyist_ID, First_Name, Last_Name, Phone from LobbyistInfo
         where First_Name like ? or Last_Name like ?
         order by Lobbyist_ID asc"""

   ids = datatier.select_n_rows(dbConn, sql, (pattern,pattern,))

   S = []
   for id in ids:
      one = Lobbyist(id[0],id[1],id[2],id[3])
      S.append(one)

   return S


##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):
   sql = """ select Lobbyist_ID, Salutation, First_Name, 
         Middle_Initial, Last_Name, 
         Suffix, Address_1, Address_2, City, State_Initial, 
         ZipCode, Country, Email, Phone, Fax
         from LobbyistInfo
         where Lobbyist_ID = ?""" 

   one = datatier.select_one_row(dbConn, sql, [lobbyist_id])

   if(one == ()):
      return None

   actual = []

   actual.append(one[0])

   if(one[1] == None):
      actual.append("")
   else:
      actual.append(one[1])

   actual.append(one[2])

   if(one[3] == None):
      actual.append("")
   else:
      actual.append(one[3])

   actual.append(one[4])

   if(one[5] == None):
      actual.append("")
   else:
      actual.append(one[5])

   actual.append(one[6])

   if(one[7] == None):
      actual.append("")
   else:
      actual.append(one[7])

   actual.append(one[8])
   actual.append(one[9])
   actual.append(one[10])
   actual.append(one[11])
   actual.append(one[12])
   actual.append(one[13])

   if(one[14] == None):
      actual.append("")
   else:
      actual.append(one[14])
   
 
   sql = """select Year from LobbyistYears 
         where Lobbyist_ID = ? """

   years = datatier.select_n_rows(dbConn,sql, [lobbyist_id])

   Y = []
   for year in years:
      Y.append(str(year[0]))

   sql = """select distinct(Employer_Name) from EmployerInfo
            join LobbyistAndEmployer on LobbyistAndEmployer.Employer_ID=EmployerInfo.Employer_ID
            where Lobbyist_ID = ? order by Employer_Name asc"""

   employ = datatier.select_n_rows(dbConn,sql,[lobbyist_id])

   E = []
   for emp in employ:
      E.append(str(emp[0]))

   sql = """select sum(Compensation_Amount) from Compensation 
   where Lobbyist_ID = ?"""

   money = datatier.select_one_row(dbConn,sql,[lobbyist_id])

   if money[0] == None:
      moneyAmount = 0
   else:
      moneyAmount = money[0]

   lobbyist = LobbyistDetails(actual[0], actual[1], actual[2], actual[3], actual[4], actual[5], actual[6], actual[7], actual[8], actual[9], actual[10], actual[11], actual[12], actual[13], actual[14], Y, E, moneyAmount)

   return lobbyist


##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total 
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid. 
#          An empty list is also returned if an internal error 
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):
   sql = """ select Compensation.Lobbyist_ID, First_Name, Last_Name, Phone, sum(Compensation_Amount) as Total_Compensation from Compensation 
         join LobbyistInfo on LobbyistInfo.Lobbyist_ID = Compensation.Lobbyist_ID
         where strftime('%Y', Period_Start) = ? and strftime('%Y', Period_End) = ?
         group by Compensation.Lobbyist_ID
         order by Total_Compensation desc
         limit ?
         """

   rows = datatier.select_n_rows(dbConn, sql, (year, year, N,))

   if rows == None:
      return None

   sql = """select Client_Name from ClientInfo
         join Compensation on Compensation.Client_ID=ClientInfo.Client_ID
         where Lobbyist_ID = ? and strftime('%Y', Period_Start) = ? and strftime('%Y', Period_End) = ?
         group by Compensation.Client_ID
         order by Client_Name asc """

   S = []

   for row in rows:
      clients = datatier.select_n_rows(dbConn,sql, (row[0], year, year,))

      C = []

      for client in clients:
         C.append(str(client[0]))
      
      one = LobbyistClients(row[0],row[1],row[2],row[3],row[4], C)

      S.append(one)

   return S




##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below), 
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):

   sql = """ select Lobbyist_ID from LobbyistInfo
            where Lobbyist_ID = ?"""

   row = datatier.select_one_row(dbConn,sql,(lobbyist_id,))

   if len(row) < 1:
      return 0


   sql = """ insert into LobbyistYears(Lobbyist_ID, Year)
         values(?,?)"""

   modified = datatier.perform_action(dbConn,sql,(lobbyist_id, year,))

   if(modified == -1):
      return 0

   return modified


##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively 
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):
   sql = """ select Lobbyist_ID from LobbyistInfo
            where Lobbyist_ID = ?"""

   row = datatier.select_one_row(dbConn,sql,(lobbyist_id,))

   if len(row) < 1:
      return 0

   sql = """ update LobbyistInfo
      set Salutation = ?
      where Lobbyist_ID = ?"""

   modified = datatier.perform_action(dbConn, sql, (salutation, lobbyist_id,))

   if(modified == -1):
      return 0

   return modified
