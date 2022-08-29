# Write-up

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*

If choosing a solution based on Virtual Machine:
PROS:
With my background, this would be the easier choice, as I would have full control of every step in the deployment, which would give me a sense of control. If something fails I would feel comfortable knowing I could troubleshoot it.
An Azure VM compared to physical hardware:
Lower cost upfront
No need to worry about hardware failure, maintaining a physical backup server etc.
It is easy to scale up without the hassle of purchasing and installing hardware
There are good options for configuring for high availability, scalability and redundancy.
CONS
The cost is higher than for the App Service
Implementing a continuous deployment process requires more work than if using the App Service
With a small app, or if you aren’t expecting any substantial growth or many changes, it might be overkill to select a VM

If choosing a solution based on App Service:
PROS:
Easy to implement continuous deployment
High availability and auto-scaling are provided out of the box.
You can limit the cost by selecting the appropriate plan (Dev/Test, Production or Isolated)
CONS
You don’t control the underlying OS
Hardware limitations of 14GB of memory and 4 vCPU cores per instance
With a complex and/or rapidly growing app, you might find the lack of control over resources is too limiting

- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*
MY CHOICE:
I selected to deploy the app through the App Service partly because this solution is new to me and I enjoyed the extra exercise. Since it is small and we are not expecting usage to grow, this is also the appropriate choice. 

### Assess app changes that would change your decision.
If, at some point, the app became very popular with increasing complexity and/or usage, it might be relevant to move it to a VM.
