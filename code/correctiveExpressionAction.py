# encoding: utf-8

import gvsig
import sys

from org.gvsig.topology.lib.spi import AbstractTopologyRuleAction

from org.gvsig.expressionevaluator import ExpressionUtils
from org.gvsig.fmap.dal import DALLocator

class CorrectiveExpressionAction(AbstractTopologyRuleAction):
    
    def __init__(self):
        AbstractTopologyRuleAction.__init__(
            self,
            "userDefinedRule",
            "CorrectiveExpressionAction",
            "Corrective Expression Action",
            "This action uses a user corrective expression for cases when User Defined rule Topology Rule it is false. This action will be different on each work"
        )

        
        self.correcExpression=None
        self.fst=None
    
    def execute(self, rule, line, parameters):
        try:
          if self.correcExpression==None:
              formula = rule.getParameters().getDynValue("CorrectiveExpression")
              if formula==None or formula=="":
                  pass
              self.correcExpression = ExpressionUtils.createExpression(formula)
              datamanager = DALLocator.getDataManager()
              self.fst = datamanager.createFeatureSymbolTable()
              self.fst.setFeature(line.getFeature1().getFeature()) #line.getFeature1() devuelve una feature reference y self.fst.setFeature necesita un feature
              self.correcExpression.execute(self.fst)
        except:
            ex = sys.exc_info()[1]
            gvsig.logger("Can't execute action. Class Name: " + ex.__class__.__name__ + ". Exception: " + str(ex), gvsig.LOGGER_ERROR)

def main(*args):
    pass