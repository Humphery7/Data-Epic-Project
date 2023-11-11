import pytest
from gspread_code import UpdateSpreadSheet
from unittest.mock import patch
import pandas as pd


class TestUpdateSpreadSheet:  
    
    @pytest.fixture
    def instantiate_class(self):
        """setup function to create
            instance of class"""
        self.inst = UpdateSpreadSheet()
        return self.inst
    
    def test_getting_data(self,instantiate_class):
        '''test to check that the data is being added to the list
         variables successfully'''
        
        #mocking selenium driver attribute for checks if code syntax is accurate
        with patch("gspread_code.driver.find_elements") as mocked_get:
            #mocked attribute driver.find_elements is assigned to list to check
            mocked_get.return_value = ['textID','yes']
            #calling getting_data function which begins to get the data from selenium
            instantiate_class.getting_data()
            #asserting all list variables were updated with first round of data gotten
            assert instantiate_class.RepoName == ['textID','yes']
            assert instantiate_class.Language == ['textID','yes']
            assert instantiate_class.Description == ['textID','yes']
            assert instantiate_class.Datetime_Posted == ['textID','yes']

            #assigning new data 
            mocked_get.return_value = [1,2]
            instantiate_class.getting_data()
            #checking all list variables retained previous data and have added new data
            assert instantiate_class.RepoName == ['textID','yes',1,2]
            assert instantiate_class.Language == ['textID','yes',1,2]
            assert instantiate_class.Description == ['textID','yes',1,2]
            assert instantiate_class.Datetime_Posted == ['textID','yes',1,2]

    def test_populating_dictionary(self,instantiate_class):
        """test to check if dictionary variable
           github_repo is succesfully being populated"""
        
        #populating list variables wiith values
        instantiate_class.RepoName = [1]
        instantiate_class.Language = [1,2]
        instantiate_class.Description = [1,2]
        instantiate_class.Datetime_Posted = [1,2]
        #calling function to populate dictionary
        instantiate_class.populating_dictionary()
        #asserting keys of dictionary are same as the number of list variables
        assert len(instantiate_class.github_repo.keys()) == 4
        #asserting values of dictionaries are identical to combination of values contained in list variables
        assert list(instantiate_class.github_repo.values()) == [[1],[1,2],[1,2],[1,2]]
        


    def test_creating_dataframe(self,instantiate_class):
        """test to check if dataframe is created successfully
           when given appropriate data and if the ValueError
           is raised when the data is not appropriate"""

        #populating dictionary variable github_repo with appropriate data
        instantiate_class.github_repo = {'test1':[2,'3'],'test2':['5','4']}
        #calling create data_frame function which creates a dataframe with dictionary github_repo
        instantiate_class.create_dataframe()
        #asserting data variable which holds the dataframe created from github_repo is equal expected dataframe
        assert instantiate_class.data.equals(pd.DataFrame({'test1':[2,'3'],'test2':['5','4']}))

        #populating github_repo variable with inappropriate data
        instantiate_class.github_repo = {'test1':[2,'3'],'test2':[5]}
        #asserting that ValueError is raised when an attempt to create a dataframe with this data is made
        with pytest.raises(ValueError):
            instantiate_class.create_dataframe()



    def test_worksheet_update(self,instantiate_class):
        """test to check if the values passed in to
           update worksheet is accurate"""
        
        #populating github_repo variable
        instantiate_class.github_repo = {'test1':[2,'3'],'test2':['5','4']}
        #creating dataframe from github_repo
        instantiate_class.create_dataframe()

        #asserting dataframe created contains expected columns
        assert instantiate_class.data.columns.tolist() == ['test1','test2']
        #asserting dataframe created contains expected values
        assert instantiate_class.data.values.tolist() == [[2,'5'],['3','4']]
