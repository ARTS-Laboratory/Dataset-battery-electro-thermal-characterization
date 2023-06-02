%10 SOC Time vs. Temperature Graph
figure()
Bat10 = plot(SOCcyle004.LabVIEWMeasurement,SOCcyle004.VarName5,'LineWidth',2)
hold on
Chamber10 = plot(SOCcyle004.LabVIEWMeasurement,SOCcyle004.VarName6, 'Linewidth',0.5)
title('Temperature During Discharge 10 SOC at 40 *C')
ylabel('Temp. *C')
xlabel('Time')
lgd10 = legend('Battery Temperature','Chamber Temperature')
set(lgd10,'Location','northwest')
uistack(Bat10,'top')
hold off

%5 SOC Time vs. Temperature Graph
figure()
Bat5 = plot(SOCcyle4.LabVIEWMeasurement,SOCcyle4.VarName5,'LineWidth',2)
hold on
Chamber5 = plot(SOCcyle4.LabVIEWMeasurement,SOCcyle4.VarName6,'LineWidth',0.5)
title('Temperature During Discharge 5 SOC at 40 *C')
ylabel('Temp. *C')
xlabel('Time')
lgd5 = legend('Battery Temperature','Chamber Temperature')
set(lgd5, 'Location', 'northwest')
uistack(Bat5,'top')
hold off

%10 SOC Time vs. Voltage Graph
figure()
plot(SOCcyle004.LabVIEWMeasurement,SOCcyle004.VarName3)
title('Voltage of 10 SOC at 40 *C')
ylabel('Voltage')
xlabel('Time')

%5 SOC Time vs. Voltage Graph
figure()
plot(SOCcyle4.LabVIEWMeasurement,SOCcyle4.VarName3)
title('Voltage of 5 SOC at 40 *C')
ylabel('Voltage')
xlabel('Time')