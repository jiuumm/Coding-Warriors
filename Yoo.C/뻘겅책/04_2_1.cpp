bool change = false;
for(int i=1; i<=n+1; i++){
    change = false;
    for(int j=1; j<=n-i; j++){
        if(a[j]>a[j+1]){
            change = true;
            int tmp = a[j];
            a[j]=a[j+1];
            a[j+1]= tmp;
        }
    }
    if (change==false){
        cout<<i<<'\n';
        break;
    }

}