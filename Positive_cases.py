from matplotlib import pyplot as plt
positive = [5,2,16,16,14,22,41,95,37,61,43,48,41,70,65,57,75,98,62,50,55]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
a_xticks = ['28th february' , '19th March' , '31st March' , '7th April' , '11th April' , '12th April' , '13th April' , '14th April' , '15th April' , '16th April' , '19th April' , '21st April' , '22nd April' , '23rd April' , '24th April' , '25th April' , '26th April' , '27th April' , '29th April' , '30th April' , '1st May']
plt.figure(figsize=(10,10))
plt.xticks(x, a_xticks)
plt.yticks(positive, positive)
plt.plot(x,positive, 'b-.')
plt.xticks(rotation=90)
plt.stem(x, positive)
plt.stem(positive, x, orientation = 'horizontal', bottom = -0.5)
plt.xlabel("Dates")
plt.ylabel("Infected Cases")
plt.title("Dapoli infected Cases")
plt.title("@itisamey", loc = 'right')
plt.show
plt.savefig('the_best_plot2.jpg')
