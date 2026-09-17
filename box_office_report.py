movie= input('Enter Movie Name:')
adult= int(input('Amount of Adult Tickets Sold:'))
adultp= adult*10
child= int(input('Amount of Child Tickets Sold:'))
childp= child*6
gross= adultp+childp
net= gross*.2
paid= gross-net
print("Movie Name:", movie)
print("Adult Tickets Sold:", adult)
print("Children Tickets Sold:", child)
print("Gross Box Office Profit: $", gross)
print("Net Box Office Profit: $", net)
print("Amount paid to Distributor: $", paid)