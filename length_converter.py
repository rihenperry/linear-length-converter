#! /usr/bin/python3

# code work by -
# Name: Rihan Stephen Pereira
# Email: rihanstephen.pereira576@myci.csuci.edu
# studentID: 002497665


from tkinter import *
from tkinter import ttk


# ---- calculation and conversion logic ---
imperial_unit = dict([('miles', 'mi'),
                      ('yards', 'yd'),
                      ('foot', 'ft'),
                      ('inches', 'in')])

metric_unit = dict([('meter', 'm'),
                    ('kilometer', 'km'),
                    ('centimeter', 'cm'),
                    ('millimeter', 'mm')])

all_measurements = {
    'm': 1, 'cm': 100, 'km': 0.001, 'mm': 1000,
    'ft': 1, 'in': 12, 'yd': round((1/3), 4), 'mi': round((1/5280), 4)
}

#  converts following US customary units  to meters which is a base value
imperial_to_metric_in_m = dict([('ft', 0.3048),
                                ('in', 0.0254),
                                ('yd', 0.9144),
                                ('mi', 1609.34)])

# converts following Metric units to feet which is a base value
metric_to_imperial_in_ft = dict([('m', 3.28084),
                                 ('cm', 0.0328084),
                                 ('km', 3280.84),
                                 ('mm', 0.00328084)])


# function to calculate any US customary unit to any Metric unit
def imperial_to_metric_calc(val, us_unit, uk_unit):
    print('change in imp')
    conversion = round((val *
                        imperial_to_metric_in_m[us_unit] *
                        all_measurements[uk_unit]), 4)
    return conversion


# function to calculate any Metric unit to any US Customary unit
def metric_to_imperial_calc(val, uk_unit, us_unit):
    print('change in meter')
    conversion = round((val *
                        metric_to_imperial_in_ft[uk_unit] *
                        all_measurements[us_unit]), 4)
    return conversion


# callback function which listens for keyrelease event on
# US/Imperial entry field. Callback used by Imperial entry box and combo box
def imperial_conv_cb(sv):
    try:
        val = float(left_align_usunitbox.get())
        us_unit = imperial_unit[left_align_usunitopts.get()]
        uk_unit = metric_unit[right_align_metricopts.get()]

        print(val, us_unit, uk_unit)
        conv_val = imperial_to_metric_calc(val,
                                           us_unit,
                                           uk_unit)
        right_align_metricbox.delete(0, 'end')
        right_align_metricbox.insert(0, conv_val)
    except ValueError:
        print('only accept integers')


# callback function which listens for keyrelease event on
# Metrics entry field. Callback used by metric entry box and combo box
def metric_conv_cb(sv):
    try:
        val = float(right_align_metricbox.get())
        uk_unit = metric_unit[right_align_metricopts.get()]
        us_unit = imperial_unit[left_align_usunitopts.get()]

        print(val, us_unit, uk_unit)
        conv_val = metric_to_imperial_calc(val,
                                           uk_unit,
                                           us_unit)
        left_align_usunitbox.delete(0, 'end')
        left_align_usunitbox.insert(0, conv_val)
    except ValueError:
        print('only accept integers')

# ---- end of calculation and conversion logic ----

# -- the root window
root = Tk()
root.title("Fixed length Calculator")

# frame inside root window
masterwidget = ttk.Frame(root, padding=(10, 10, 10, 10))
frame = ttk.Frame(masterwidget, borderwidth=5, width=200, height=100)

center_equivalence_symbol = ttk.Label(masterwidget, text="=")

# metric length gui widget configure
right_align_meterlbl = ttk.Label(masterwidget, text="Metric length")

onchange_metric_entry = StringVar()
right_align_metricbox = ttk.Entry(masterwidget,
                                  textvariable=onchange_metric_entry,
                                  width="10")
right_align_metricbox.bind("<KeyRelease>", metric_conv_cb)

right_metric_list = StringVar()
right_align_metricopts = ttk.Combobox(masterwidget, state="readonly",
                                      textvariable=right_metric_list,
                                      values=tuple(metric_unit.keys()),
                                      width="10")

right_align_metricopts.current(0)
right_align_metricopts.bind("<<ComboboxSelected>>", metric_conv_cb)
# end of metric length gui widgets

# imperial length gui widgets configure
left_align_usunitlbl = ttk.Label(masterwidget, text="Imperial length")

onchange_usunit_entry = StringVar()
left_align_usunitbox = ttk.Entry(masterwidget,
                                 textvariable=onchange_usunit_entry,
                                 width="10")
left_align_usunitbox.bind("<KeyRelease>", imperial_conv_cb)

left_usunit_list = StringVar()
left_align_usunitopts = ttk.Combobox(masterwidget, state="readonly",
                                     textvariable=left_usunit_list,
                                     values=tuple(imperial_unit.keys()),
                                     width="10")
left_align_usunitopts.current(2)
left_align_usunitopts.bind("<<ComboboxSelected>>", imperial_conv_cb)
# end of imperial length gui widgets configure

# N, W, E, S regions allow us to place widgets correctly on the grid
masterwidget.grid(column=0, row=0, sticky=(N, W, E, S))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, W, E, S))

left_align_usunitlbl.grid(column=0, row=0, columnspan=2, sticky=(S, W),
                          pady=3, padx=3)
left_align_usunitbox.grid(column=0, row=1, sticky=(W, N), pady=3, padx=3)
left_align_usunitopts.grid(column=1, row=1, sticky=(W, E, N), pady=3, padx=3)

center_equivalence_symbol.grid(column=2, row=1, sticky=N, pady=3, padx=3)

right_align_meterlbl.grid(column=3, row=0, columnspan=2, sticky=(S, W),
                          pady=3, padx=3)
right_align_metricbox.grid(column=3, row=1, sticky=(N, E), pady=3, padx=3)
right_align_metricopts.grid(column=4, row=1, sticky=(N, E), pady=3, padx=3)

# This code is used for resizing window and used for scaling &
# keeping in place the widgets
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
masterwidget.columnconfigure(0, weight=3)
masterwidget.columnconfigure(1, weight=3)
masterwidget.columnconfigure(2, weight=3)
masterwidget.columnconfigure(4, weight=3)
masterwidget.rowconfigure(0, weight=3)
masterwidget.rowconfigure(1, weight=3)

# initial focus on Imperial unit entry box
left_align_usunitbox.focus()

# start main event loop
root.mainloop()
