## TP00RU03CP0000 Test the user check expression if all 2D polygon have one internal 2D point.

[First, check the open issues of this test](https://redmine.gvsig.net/redmine/projects/gvsig-desktop/issues?utf8=%E2%9C%93&set_filter=1&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=subject&op%5Bsubject%5D=%7E&v%5Bsubject%5D%5B%5D=TP00RU03CP0000&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=subject&c%5B%5D=assigned_to&c%5B%5D=updated_on&group_by=)

### Description

This test case checks the topology rule when we use correct 2D datasets. The case seeks a correct final result if we use corrects datasets and a right check expression. All polygons have al least one internal point and does the check expression True.

### Requirements

1. Have *gvSIG desktop 2.5.1* and *Topology framework plugin* installed.
2. Have acces to [**TP00RU03CP0000_pol2D_C.csv**](https://github.com/jolicar/TopologyRuleUserDefinedRule/blob/master/testing/cases/TP00_TopologyRules/RU03_UserDefinedRule/CP0000_UDR_C/TP00RU03CP0000_pol2D_C.csv) and [**TP00RU03CP0000_pts2D_C.csv**](https://github.com/jolicar/TopologyRuleUserDefinedRule/blob/master/testing/cases/TP00_TopologyRules/RU03_UserDefinedRule/CP0000_UDR_C/TP00RU03CP0000_pts2D_C.csv) files.

### Steps...

1. Load the layer **TP00RU03CP0000_pol2D_C.csv** in the view.
2. Load the layer **TP00RU03CP0000_pts2D_C.csv** in the view.
3. Create a new empty topology plan.
4. Fill the basic topology plan data.
5. Add the **TP00RU03CP0000_pol2D_C.csv** file like a dataset.
6. Add a new rules parameters on Rules tab.
7. On those rule parameters identify the *primary dataset*, the *User defined topology rule*. 
8. If *User defined topology rule* is selected, the UDR Parameters tab will be enabled.
9. Add the user check expression with expression builder; EXISTS( SELECT * FROM TP00RU03CP0000_pts2D_C WHERE ST_INTERSECTS(ST_FORCE2D(TP00RU03CP0000_pts2D_C.GEOMETRY), ST_FORCE2D(GEOMETRY())) LIMIT 1).
10. Click on the "Ok" button.
11. Click on the "Ok" button to finish the topology plan creation.
12. Execute the topology plan.

### Expected result

The expected results are the *Inspector de errores del Plan de topologia* window empty. This interface has no records.


### Bug report


In case the obtained results are not correct, you can report an issue on *redmine* of *gvSIG deskop*. You can locate at
https://redmine.gvsig.net/redmine/projects/gvsig-desktop/issues .

[Open a a new issue of this test](https://redmine.gvsig.net/redmine/projects/gvsig-desktop/issues/new?issue[subject]=TP00RU03CP0000+Test+the+user+check+expression+if+all+2D+polygon+have+one+internal+2D+point)