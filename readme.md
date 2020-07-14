# User Defined Rule Topology Rule

* **Rule type:** *All geometry type rule*
* **Primary dataset:** Polygon, line or point dataset (2D, 2DM, 3D and 3DM) (*Multygeometry allowed*)
* **Secundary dataset:** Polygon, line or point dataset (2D, 2DM, 3D and 3DM) (*Multygeometry allowed*)
* **Brief description:** UDR is a especial topology rule. This rule allows the user to define the parameter, check parameters and the formula to correct it. This statement can be used in all the topology rules created or not in the software. It depends if we know the necessary check parameters. This is too basic, the features of a layer are evaluated for the check parameters and it gives a boolean. If the result is *False*, the rule create a entry in the error report. If the result is *True*, the process will continue with the next feature. When all features are evaluated, the rule checks the error report and does an action, remove the feature or apply the corrective formula. In 2DM, 3D and 3DM formats, the Z coordinate or M coordinate are ignored.
* **Limitations:** The two datasets cant have a different projection.
* **Rule behavior:** 
  - If the Tolerance equals zero, the rule does as above. If the tolerance is greater than zero, the script does a dataset 1 feature buffer with tolerance value. If the dataset 2 feature fullfills the check parameters whit the new dataset 1 polygon, the rule return *True*.

* **Potential fixes actions:** 
  - **Delete** The delete action removes features for cases when *User Defined rule* Topology Rule it is false.
  - **User correction formula** This option will be different on each work.

#### [*Back to GSoC2020 Project Wiki*](https://github.com/jolicar/GSoC2020/wiki/GSoC2020-New-rules-for-the-Topology-Framework-in-gvSIG-Desktop)