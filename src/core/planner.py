from langchain_core.messages import HumanMessage,AIMessage
from src.chains.itinerary_chain import generate_itineary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException


logger = get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages=[]
        self.city=""
        self.intrests=[]
        self.itineary = ""
        
        logger.info("Initializing TravelPlanner instance")
        
    def set_city(self,city:str):
        try:
            self.city = city
            self.messages.append(HumanMessage(content=city))
            logger.info("city set successfully")
            
        except Exception as e:
            logger.error(f"Error while setting city: {e}")
            raise CustomException("Failed to set city",e)
        
    def set_intrests(self,intrests_str:str):
        try:
            self.intrests = [i.strip() for i in  intrests_str.split(",")]
            self.messages.append(HumanMessage(content=intrests_str))
            logger.info("intrests also set successfully")
        except Exception as e:
            logger.error(f"Error while setting intrests: {e}")
            raise CustomException("Failed to set intrests",e)
        
    def create_itineary(self):
        try:
            logger.info(f"Generating itineary for {self.city} and for intrest : {self.intrests}")
            itineary = generate_itineary(self.city, self.intrests)
            self.itineary = itineary
            self.messages.append(AIMessage(content=itineary))
            logger.info("itineary generated successfully")
            return itineary
        except Exception as e:
            logger.error(f"Error while generating itineary: {e}")
            raise CustomException("Failed to generate itineary",e)