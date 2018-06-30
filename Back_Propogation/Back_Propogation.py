import random,numpy
import math
from prettytable import PrettyTable

#********************* CREATED INPUT NEURONS *****************************************
def Create_Input_Values(Input):
    for i in range(int(Input)):
    	Input_nam_val = []
        Input_value = random.uniform(0.01,0.99)
	Input_value = round(Input_value, 4)
	Input_nam_val.append('Input' + str(i+1))
	Input_nam_val.append(Input_value)
        Inputs.append(Input_nam_val)

Inputs = []
Input = int(raw_input("Enter the No of Inputs Neurons = "))
Create_Input_Values(Input)


x = PrettyTable()
x.field_names = ["No_of_Input_Neurons","Weights"]
for i in range(len(Inputs)):
	x.add_row(Inputs[i])

print x

#********************* CREATED HIDDEN NEURONS ***************************************
def Create_Hidden_Values(Input,Hidden):
	k = 0
	for i in range(int(Input)):
		for j in range(int(Hidden)):
			Hidden_nam_val = []
			Hidden_value = random.uniform(0.01,0.99)
			Hidden_value = round(Hidden_value, 4)
			Hidden_nam_val.append('Input' + str(i+1))
			Hidden_nam_val.append(Hidden_value)
			Hidden_nam_val.append('Hidden' + str(j+1))
			Hidden_nam_val.append('Weight' + str(k+1))
			k += 1
			Hiddens.append(Hidden_nam_val)

Hiddens = []
Hidden = int(raw_input("Enter the No of Hidden Neurons = ")) 
Create_Hidden_Values(Input,Hidden)

x = PrettyTable()
x.field_names = ["From_Input","Weights","To_Hidden","Weight_Name"]
for i in range(len(Hiddens)):
	x.add_row(Hiddens[i])
print x

#********************* CREATED OUTPUT NEURONS ***************************************
def Create_Output_Values(Hidden,Output):
	k = len(Hiddens)
	for i in range(int(Hidden)):
		for j in range(int(Output)):
			Outputs_nam_val = []
			Output_value = random.uniform(0.01,0.99)
			Output_value = round(Output_value, 4)
			Outputs_nam_val.append('Hidden' + str(i+1))
			Outputs_nam_val.append(Output_value)
			Outputs_nam_val.append('Output' + str(j+1))
			Outputs_nam_val.append('Weight' + str(k+1))
			k += 1
			Outputs.append(Outputs_nam_val)

Outputs = []
Output = int(raw_input("Enter the No of Output Neurons = "))
Create_Output_Values(Hidden,Output)

x = PrettyTable()
x.field_names = ["From_Hidden","Weights","To_Output","Weight_Name"]
for i in range(len(Outputs)):
	x.add_row(Outputs[i])
print x

#********************* EXPECTED OUTPUT ***************************************
def Create_Expected_Output(Output):
	for i in range(int(Output)):
		Out_nam_val = []
        	Out_value = random.uniform(0.01,0.99)
		Out_value = round(Out_value, 4)
		Out_nam_val.append('Expected_Output' + str(i+1))
		Out_nam_val.append(Out_value)
        	Expected_Output.append(Out_nam_val)

Expected_Output = []
Create_Expected_Output(Output)

x = PrettyTable()
x.field_names = ["No_of_Output_Neurons","Expected_Value"]
for i in range(len(Expected_Output)):
	x.add_row(Expected_Output[i])
print x

#*****************************************************************************
H_B = random.uniform(0.01,0.99)
Hidden_Bias = round(H_B, 4)
O_B = random.uniform(0.01,0.99)
Output_Bias = round(O_B, 4)

"""Hidden = 2
Output = 2
Inputs = [['Input1', 0.05], ['Input2', 0.10]]
Hiddens = [['Input1', 0.15, 'Hidden1', 'Weight1'], ['Input1', 0.25, 'Hidden2', 'Weight2'], ['Input2', 0.20, 'Hidden1', 'Weight3'], ['Input2', 0.30, 'Hidden2', 'Weight4']]
Outputs = [['Hidden1', 0.40, 'Output1', 'Weight5'], ['Hidden1', 0.50, 'Output2', 'Weight6'], ['Hidden2', 0.45, 'Output1', 'Weight7'], ['Hidden2', 0.55, 'Output2', 'Weight8']]
Expected_Output = [['Expected_Output1', 0.01], ['Expected_Output2', 0.99]]
Hidden_Bias = 0.35
Output_Bias = 0.60"""
#******************** CALCULATING FORWARD PROPOGATION *****************************
def Calc_net_input(Inputs,Hiddens,Outputs,iteration):
	#*********** Calculate Total Net Input For Hidden **************************
	while(True):
		print "Iteration = " + str(iteration+1)
		Calc_net = []
		for i in range(int(Hidden)):
			Calc_nt = []
			for j in range(len(Hiddens)):
				if ('Hidden' + str(i+1)) in Hiddens[j]:
					Calc_nt.append(Hiddens[j][1])
			Calc_net.append(Calc_nt)
		F_Calc_Net,Calc_net_H = [],[]
		for i in range(len(Calc_net)):
			Calc_nt = []
			for j in range(len(Inputs)):
				Net_IP = float(Calc_net[i][j]) * float(Inputs[j][1])
				Net_IP = round(Net_IP, 4)
				Calc_nt.append(Net_IP)
			s = sum(Calc_nt) + (Hidden_Bias * 1)
			s = round(s, 4) 
			F_Calc_Net.append(s)		
		for i in range(len(F_Calc_Net)):
			Calc_nt1 = []
			Calc_nt1.append('Hidden' + str(i+1))		 		
			Calc_nt1.append(F_Calc_Net[i])
			Calc_net_H.append(Calc_nt1)

		x = PrettyTable()
		x.field_names = ["Net_Input_for_Hidden","Values"]
		for k in range(len(Calc_net_H)):
			x.add_row(Calc_net_H[k])
		print x
	#*********** Calculate Output for Hidden Using Logistic Function ************
		H_out = []
		for i in range(len(Calc_net_H)):
			H = []
			logistic = 1/(1 + (numpy.exp(-Calc_net_H[i][1])))
			logistic = round(logistic, 4)
			H.append('Hidden' + str(i+1))
			H.append(logistic)
			H_out.append(H)
	
		x = PrettyTable()
		x.field_names = ["Logistic_Output_for_Hidden","Values"]
		for k in range(len(H_out)):
			x.add_row(H_out[k])
		print x

	#************ Calcuate Total Net Input For Output ********************
		Calc_net_Output = []
		for i in range(int(Output)):
			Calc_nt = []
			for j in range(len(Outputs)):
				if ('Output' + str(i+1)) in Outputs[j]:
					Calc_nt.append(Outputs[j][1])
			Calc_net_Output.append(Calc_nt)
		F_Calc_Net,Calc_net_O = [],[]
		for i in range(len(Calc_net_Output)):
			Calc_nt = []
			for j in range(len(H_out)):
				Net_IP = float(Calc_net_Output[i][j]) * float(H_out[j][1])
				Net_IP = round(Net_IP, 4)
				Calc_nt.append(Net_IP)
			s = sum(Calc_nt) + (Output_Bias * 1)
			s = round(s, 4) 
			F_Calc_Net.append(s)		
		for i in range(len(F_Calc_Net)):
			Calc_nt1 = []
			Calc_nt1.append('Output' + str(i+1))		 		
			Calc_nt1.append(F_Calc_Net[i])
			Calc_net_O.append(Calc_nt1)

		x = PrettyTable()
		x.field_names = ["Net_Input_for_Output","Values"]
		for k in range(len(Calc_net_O)):
			x.add_row(Calc_net_O[k])
		print x
	#*************** Calculate Output For Output Using Logistic Function *******
		O_out = []
		for i in range(len(Calc_net_O)):
			O = []
			logistic = 1/(1 + (numpy.exp(-Calc_net_O[i][1])))
			logistic = round(logistic, 4)
			O.append('Output' + str(i+1))
			O.append(logistic)
			O_out.append(O)
	
		x = PrettyTable()
		x.field_names = ["Logistic_Output_for_Output","Values"]
		for k in range(len(O_out)):
			x.add_row(O_out[k])
		print x
	#************* Calculate Error For Output Using Squared Error Function *******
		Tar_Out = []
		for i in range(len(O_out)):
			TarOut = []
			Tar = 0.5*(float(Expected_Output[i][1]) - float(O_out[i][1]))**2
			Tar = round(Tar, 4)
			TarOut.append("Error_output" + str(i+1))
			TarOut.append(Tar)
			Tar_Out.append(TarOut)

		x = PrettyTable()
		x.field_names = ["Errors","Values"]
		for k in range(len(Tar_Out)):
			x.add_row(Tar_Out[k])
		print x
	#************** Calculate Total Error For Neural Network ***************
		sum1 = 0.0000
		for i in range(len(Tar_Out)):
			sum1 = sum1 + Tar_Out[i][1]
		sum1 = round(sum1, 4)
	
		x = PrettyTable()
		x.field_names = ["Total_Error"]
		x.add_row([sum1])
		print x
		chk = round(sum1, 3)
		if chk == 0.000:
			print Expected_Output
			break
	#*************************************************************************
	#**********************	BACK-PROPOGATION *********************************
	#*************************************************************************
	#*************** CALCULATE OUTPUT LAYER USING CHAIN RULE *****************
		chain_rule = []
		eta = 0.5
		for i in range(len(O_out)):
			ch_rule = []
			for j in range(len(Outputs)):
				if O_out[i][0] == Outputs[j][2]:
					a = -(float(Expected_Output[i][1]) - float(O_out[i][1]))
					a = round(a, 4)
					ch_rule.append(a)
					b = O_out[i][1] * (1 - float(O_out[i][1]))
					b = round(b, 4)
					ch_rule.append(b)
					for k in range(len(H_out)):
						if Outputs[j][0] == H_out[k][0]:
							c = H_out[k][1]
							ch_rule.append(c)
							d = float(a) * float(b) * float(c)
							d = round(d, 4)
							ch_rule.append(d)
							e = Outputs[j][1] - eta * float(d)
							e = round(e, 4)
							ch_rule.append(e)
							f = Outputs[j][3]
							ch_rule.append(f)
							chain_rule.append(ch_rule)
							ch_rule = []
		x = PrettyTable()
		x.field_names = ["T_Er_Ch_WRT_O","O_Ch_WRT_T_Net_I/P","T_Net_I/P_Ch_WRT_Weight","Chain_Rule","D_Er_Mult_ETA/New_Weights","Weights"]
		for k in range(len(chain_rule)):
			x.add_row(chain_rule[k])
		print x
	#************** CALCULATE HIDDEN LAYER USING CHAIN RULE *****************
		kk,kkk,kkk1,kkk2,f_result,chain_rule_H =[],[],[],[],[],[]
		for i in range(len(Hiddens)):
			for j in range(len(Outputs)):
				if Hiddens[i][2] == Outputs[j][0]:
					for k in range(len(chain_rule)):
						if Outputs[j][3] == chain_rule[k][5]:
							l = float(chain_rule[k][0]) * float(chain_rule[k][1]) * float(Outputs[j][1])
							l = round(l, 4)
							kk.append(l)
			s = sum(kk)
			s = round(s, 4)
			kkk.append(s)
			kk = []
		for i in range(len(Inputs)):
			for j in range(len(Hiddens)):
				if Inputs[i][0] == Hiddens[j][0]:
					for k in range(len(H_out)):
						if Hiddens[j][2] == H_out[k][0]:
							kkk1.append(H_out[k][1])
							kkk2.append(Inputs[i][1])
		
		xyz = map(list, zip(kkk,kkk1,kkk2))
		for i in range(len(xyz)):
			result = numpy.prod(xyz[i])
		        result = round(result, 4)
			f_result.append(result)
		for i in range(len(Hiddens)):
			z = int(Hiddens[i][1]) - (eta * f_result[i])
			z = round(z, 4)
			chain_rule_H.append(z)
	
		x = PrettyTable()
		x.field_names = ["Weights","Values"]
		chain_rule_H = map(str, chain_rule_H)
		F_chain_rule_H,Final_chain_rule_H = [],[]
		for i in range(len(chain_rule_H)):
			a = "Weight" + str(i+1)
			F_chain_rule_H.append(a)
			F_chain_rule_H.append(chain_rule_H[i])
			Final_chain_rule_H.append(F_chain_rule_H)
			F_chain_rule_H = []
		for k in range(len(Final_chain_rule_H)):
			x.add_row(Final_chain_rule_H[k])
		print x
		for i in range(len(Final_chain_rule_H)):
			Hiddens[i][1] = float(Final_chain_rule_H[i][1])
		x = PrettyTable()
		x.field_names = ["From_Input","Weights","To_Hidden","Weight_Name"]
		for i in range(len(Hiddens)):
			x.add_row(Hiddens[i])
		print x
		for i in range(len(chain_rule)):
			Outputs[i][1] = chain_rule[i][4]
		x = PrettyTable()
		x.field_names = ["From_Hidden","Weights","To_Output","Weight_Name"]
		for i in range(len(Outputs)):
			x.add_row(Outputs[i])
		print x	
		iteration += 1
		
			
Calc_net2 = []
iteration = 0
Calc_net_input(Inputs,Hiddens,Outputs,iteration)
