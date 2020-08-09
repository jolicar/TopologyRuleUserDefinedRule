# encoding: utf-8

import gvsig
import sys

from gvsig import uselib #para cargar plugins, scripting no tiene cargados todos los plugins
uselib.use_plugin("org.gvsig.topology.app.mainplugin")

from org.gvsig.expressionevaluator import GeometryExpressionEvaluatorLocator, ExpressionEvaluatorLocator
from org.gvsig.topology.lib.api import TopologyLocator
from org.gvsig.topology.lib.spi import AbstractTopologyRule

from org.gvsig.expressionevaluator import ExpressionUtils
from org.gvsig.fmap.dal import DALLocator

from deleteFeatureAction import DeleteFeatureAction
from correctiveExpressionAction import CorrectiveExpressionAction

class UserDefinedRule(AbstractTopologyRule):


  def __init__(self, plan, factory, tolerance, dataSet1):
      AbstractTopologyRule.__init__(self, plan, factory, tolerance, dataSet1)
      self.addAction(DeleteFeatureAction())
      self.addAction(CorrectiveExpressionAction())
      
      self.checkExpression=None
      self.fst=None

  def check(self, taskStatus, report, feature1):
      try:
          if self.checkExpression==None:
              formula = self.getParameters().getDynValue("CheckExpression")
              self.checkExpression = ExpressionUtils.createExpression(formula)
              datamanager = DALLocator.getDataManager()
              self.fst = datamanager.createFeatureSymbolTable()
          self.fst.setFeature(feature1)
          x=self.checkExpression.execute(self.fst)
          if not x:
              report.addLine(self,
                self.getDataSet1(),
                None,
                feature1.getDefaultGeometry(),
                feature1.getDefaultGeometry(),
                feature1.getReference(),
                None,
                -1,
                -1,
                False,
                "This feature does False the Check Expression",
                ""
              )
      except:
          ex = sys.exc_info()[1]
          gvsig.logger("Can't execute rule. Class Name: " + ex.__class__.__name__ + ". Exception: " + str(ex), gvsig.LOGGER_ERROR)



