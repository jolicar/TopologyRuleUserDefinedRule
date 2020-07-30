# User Defined Rule Topology Rule

* **Rule type:** *All data type*
* **Primary dataset:** Any dataset (2D, 2DM, 3D and 3DM) (*Multygeometry allowed*)
* **Brief description:** This rule allows the user to define a data check expression and another expression to correct it. The dataset features are evaluated for the check expression and it gives a boolean. If the result is *False*,the feature dont fulfill the rule and it creates a entry in the error report. If the result is *True*, the feature fulfills the expression. On *Inspector de errores del Plan de topologia* window we can remove the feature or apply the corrective expression. 
* **Limitations:** The check and corrective expression are create on gvSIG Cosa languaje.

* **Potential fixes actions:** 
  - **Delete** The delete action removes features for cases when *User Defined rule* Topology Rule it is false.
  - **User corrective expression** This option will be different on each work.

#### [*Back to GSoC2020 Project Wiki*](https://github.com/jolicar/GSoC2020/wiki/GSoC2020-New-rules-for-the-Topology-Framework-in-gvSIG-Desktop)