%% 输入自变量n的数量级
n = logspace(0,15,16);

%% 定义函数
f_constant = n - n + 10e2;
f_logarithm = log2(n);
f_linear = n;
f_nlogn = n .* log2(n);
f_quadratic = n.^2;
f_cubic = n.^3;
f_exponentional = 2.^n;

%% 作图
loglog(n,f_constant,'-d');
hold on;
loglog(n,f_logarithm,'-o');
loglog(n,f_linear,'-s');
loglog(n,f_nlogn,'-p');
loglog(n,f_quadratic,'-h');
loglog(n,f_cubic,'-v');
loglog(n,f_exponentional,'-<');
axis([1 10e15 1 10e44]);
xlabel('n');
ylabel('f(n)');
hold off