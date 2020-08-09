# encoding: utf-8

import gvsig
import sys

from gvsig import uselib
uselib.use_plugin("org.gvsig.topology.app.mainplugin")

from org.gvsig.fmap.geom import Geometry
from org.gvsig.tools.util import ListBuilder
from org.gvsig.topology.lib.api import TopologyLocator
from org.gvsig.topology.lib.spi import AbstractTopologyRuleFactory, RuleResourceLoaderUtils
from org.gvsig.tools import ToolsLocator

from java.io import File

from userDefinedRule import UserDefinedRule

class UserDefinedRuleFactory(AbstractTopologyRuleFactory):
      
    def __init__(self):
        AbstractTopologyRuleFactory.__init__(
            self,
            "UserDefinedRule",
            "User defined rule GSoC2020",
            "This rule allows the user to define a data check expression and another expression to correct it. The dataset features are evaluated for the check expression and it gives a boolean. If the result is False,the feature dont fulfill the rule and it creates a entry in the error report. If the result is True, the feature fulfills the expression. On Inspector de errores del Plan de topologia window we can remove the feature or apply the corrective expression. \n\n The check and corrective expression are create on gvSIG Cosa languaje.",
            None
        )

        pathName = gvsig.getResource(__file__,'UserDefinedRule.json')
        url = File(pathName).toURL()
        gvsig.logger(str(url))
        json = RuleResourceLoaderUtils.getRule(url)
        self.load_from_resource(url, json)
        
        dynObjectManager = ToolsLocator.getDynObjectManager()
        self.parametersDefinition = dynObjectManager.createDynClass("UserDefinedRuleParameters", "UserDefinedRuleParameters")
        self.parametersDefinition.addDynFieldString("CheckExpression").setLabel("Check expression").setDescription("")
        self.parametersDefinition.addDynFieldString("CorrectiveExpression").setLabel("Corrective expression").setDescription("")
    
    def createRule(self, plan, dataSet1, dataSet2, tolerance):
        rule = UserDefinedRule(plan, self, tolerance, dataSet1)
        return rule

    def hasRuleParameters(self):
        return True

    def createRuleParameters(self):
        dynObjectManager = ToolsLocator.getDynObjectManager()
        parameters=dynObjectManager.createDynObject(self.parametersDefinition)
        return parameters

def selfRegister():
    try:
        manager = TopologyLocator.getTopologyManager()
        manager.addRuleFactories(UserDefinedRuleFactory())
    except:
        ex = sys.exc_info()[1]
        gvsig.logger("Can't register rule. Class Name: " + ex.__class__.__name__ + ". Exception: " + str(ex), gvsig.LOGGER_ERROR)

def main(*args):
    pass