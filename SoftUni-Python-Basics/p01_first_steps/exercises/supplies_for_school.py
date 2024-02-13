number_of_pen = int(input())
number_of_markers = int(input())
litres_of_cleaning_agent = int(input())
discount = float(input())

package_pen = 5.80
package_markers = 7.20
cleaning_agent_per_litre = 1.20

total_pen_price = number_of_pen * package_pen
total_marker_price = number_of_markers * package_markers
total_cleaning_agent = litres_of_cleaning_agent * cleaning_agent_per_litre

no_discount_sum = total_cleaning_agent + total_marker_price + total_pen_price
discount_rate = discount / 100
final_price = no_discount_sum - (no_discount_sum * discount_rate)

print(final_price)
