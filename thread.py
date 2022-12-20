import os
import sys



from api import GPT, Example, UIConfig
from api import demo_web_app

question_prefix = "Input: "
answer_prefix = "Output: "


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
temperature=0.5,
max_tokens=100,
input_prefix=question_prefix,
output_prefix=answer_prefix,
append_output_prefix_to_query=False)

gpt.add_example(Example("""Input:
Introducing ANYbotics Workforce – Intuitive Robot Control from Any Device.
ANYbotics introduces Workforce, a new and intuitive user interface (UI) that enables any facility personnel to operate ANYmal from any device.
Workforce enables you to set-up and verify missions which reduces the time to deploy ANYmal to a few hours.
Get started with the tablet provided or access Workforce from any device with a web browser for easy automation of routine inspection tasks at scale.
Key Features:
- Streamlined workflow enables a single operator to set up complex inspection missions quickly.
- View and verify real-time robot data such as 3D scan results and data from visual, thermal, and acoustic measurements.
- Intuitive and accurate robot control during mission setup with built-in safety checks.
- Work with the ruggedized tablet shipped with ANYmal (durable, water- and dust-resistant) or use existing company devices.
- Access ANYbotics Workforce through a browser from any device (no downloads or installation required)""",
"""Output: 
1/2 Introducing @ANYbotics Workforce – Intuitive Robot Control from Any Device! This revolutionary UI enables facility personnel to quickly & easily set up & verify missions, reducing the time to deploy #ANYmal to a few hours. 
2/2 Key features of the @ANYbotics Workforce include a streamlined workflow, real-time robot data, intuitive & accurate robot control and access through a browser from any device. Get started with the tablet provided or use existing company devices!"""))

gpt.add_example(Example("""Input:
High-Precision Reality Capture with Leica BLK ARC
ANYbotics partners with Leica Geosystems to automate high-precision reality capture and 3D scanning. ANYmal’s Leica BLK ARC payload integration creates detailed 3D models during regular inspections.
Digital twins and inventory models can be easily created, and for dynamic sites, infrastructure progress checks and 3D model updates can be done daily. This makes on-demand 3D models available to operators, more accurately, cheaper and quicker.
Compared to outsourced facility scanning, the BLK ARC – ANYmal solution is estimated to be seven times more cost efficient.
Key Features
- Create accurate digital twins of your facility effortless while ANYmal performs its autonomous inspection mission
- Seamless BLK ARC operation from the ANYmal UI – control the scanner acquisition, visualize and manage your scans from a single interface
- Visualize, measure, export, and create your own custom workflows making use of the Leica software ecosystem""",
""""Output:
1/2 High-precision reality capture & 3D scanning is made easier with @ANYbotics partnership with Leica Geosystems! ANYmal's Leica BLK ARC payload integration creates detailed 3D models during regular inspections, making digital twins & inventory models easily accessible. 
2/2 Key features include the seamless BLK ARC operation from the ANYmal UI, visualization, measurement & export capabilities. Compared to outsourced facility scanning, the BLK ARC - ANYmal solution is estimated to be 7x more cost-efficient!"""))

gpt.add_example(Example("""Input:
ANYmal X Becomes Accessible to a Broader User-Base
ANYbotics opens the availability of its ANYmal X inspection solution at the SPRINT Robotics World Conference for Inspection and Maintenance Robotics. Participants in the ANYmal X Early Adopter Program (EAP) have been employing the ANYmal X inspection solution for several months.
Asset operators beyond the EAP can now order ANYmal X and include Ex-proof, autonomous and mobile robots in their inspection and operational planning.
The Only Solution that Scales Robotic Inspections in Ex-rated Facilities
Oil & Gas and Chemical operations are complex, and ensuring the highest safety standards is paramount. Operators require Ex-certified, intrinsically safe equipment (ATEX or IECEx certification) in most of the process areas.
Compared to tracked and wheeled robots, only legged robots can provide the level of mobility and autonomy required to navigate the intricate and complex multi-level structures of Oil & Gas and Chemical facilities, including industrial stairs and confined spaces.
ANYmal X is powered by AI-based locomotion, navigation, and inspection intelligence, which allows it to conduct seamless, automated inspections in very complex environments.

As the only Ex-certified and scalable robotic solution, ANYmal X is a real game changer for end-users and solution integrators, as it helps to close the digitalization gap and enables unmanned facilities.
ANYmal X closes an important technical gap, conducting automated inspections in very complex environments, with stairs and tight passages, and this in combination with Ex-zones, that’s a novelty! – Peter Welter, Automation Manager, BASF.

Deployment of the Game Changing ANYmal X Inspection Solution
The EAP enables end-users to implement the ANYmal X inspection solution efficiently. Several global innovation leaders have started deploying ANYmal X at their Ex-rated facilities.
The global energy company PETRONAS has spearheaded the integration of autonomous, legged Ex-certified robots by partnering with ANYbotics on ANYmal X since 2019. The PETRONAS ANYmal X roll-out program is progressing well in its overall deployment plan, which includes upstream platforms, terminals, and downstream plants.
Having ANYmal X Ex-certified drives innovation in R&D to go beyond conventional applications, thus improving the safety and efficiency of our operations. – Iskandar Al-Thani Mahmood, Manager (Robotics), PETRONAS.

Ramping up Production for Increasing Demand
The first deliveries of ANYmal X units to selected customers will commence in mid-2023. The opening of industry-wide order acceptance will further accelerate industry adoption.
With over 500 ANYmal X units already reserved by its EAP participants, ANYbotics has already implemented a program through its global manufacturing partner network, to scale production output to meet future demand.""",
""""Output:
1/4 @ANYbotics opens the availability of its ANYmal X inspection solution at the SPRINT Robotics World Conference, allowing asset operators to order the Ex-proof, autonomous & mobile robots & include them in their inspection & operational planning. 
2/4 ANYmal X is powered by AI-based locomotion, navigation & inspection intelligence, which allows it to conduct seamless, automated inspections in complex environments with stairs & tight passages, making it the only Ex-certified & scalable robotic solution. 
3/4 Several global innovation leaders have started deploying ANYmal X at their Ex-rated facilities, with the PETRONAS roll-out program progressing well. First deliveries of ANYmal X to customers will commence in mid-2023, with over 500 units already reserved.
4/4 @ANYbotics has implemented a program to scale production output to meet future demand, accelerating industry adoption & driving innovation to improve safety & efficiency of operations. Get ready for the game-changing ANYmal X inspection solution!"""))

# Define UI configuration
config = UIConfig(
    description="GPT3 Threadoor",
    button_text="Generate Tweets",
    placeholder="Add your raw text here",
    show_example_form=True,
)

demo_web_app(gpt, config)
