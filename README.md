# team-tracker
Search football teams and get information about them . Made with python , flask , js , html .
This is a 2 tier application which is used for me to deploy it to azure via a VM or Azure Functions. So it is basically a learning project , so dont mind the frontend (its very basic and lame) and the backend is written just to get data from the database( sqlite3 is used as a database) and display it to the frontend and this is achieved by using the fetch() function in javascript.
<h4>These are the steps used to deploy the application to the cloud:</h4>
<li>Create a new resource group in the Azure portal. A resource group is a logical container that you can use to group related resources in Azure.</li>

<li>Create a new virtual machine (VM) in the resource group. You can choose a VM image that is pre-configured with the operating system and software that you need for your application.</li>

<li>Configure the VM with the necessary settings, such as the size and number of cores. You may also need to configure the network settings, such as the virtual network and public IP address.</li>

<li>Connect to the VM using Remote Desktop Protocol (RDP) or Secure Shell (SSH). This will allow you to install the necessary software and configure the operating system.</li>

<li>Install the necessary software on the VM, including the database server and application server.</li>

<li>Deploy your application to the VM. This will typically involve copying the application files to the VM and configuring the application server to run the application.</li>

<h3> The final output ( I know it looks bad ) after deploying it to a virtual machine in Azure</h3>
<img src="https://github.com/rghdrizzle/team-tracker/blob/main/Screenshot%20(87).png">
<p> As you can see when I search for a particular team , PSG from the image above , it gets the data from the database and displays it in the frontend . Yes , the output doesnt seem very pleasing nor pretty but the purpose here really is just to have a working 2 tier application so I can deploy it to Azure .</p>
<p>-------Improvements to the application might come later--------</p>
