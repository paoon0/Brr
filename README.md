## 学士研究の過程で作成したコンテナアプリケーションの一部
NginxがWebサーバの役割を担い,静的ファイルを提供,APIとの通信をプロキシ  
APIはタスク管理に関するサービスを提供し、MySQLともやり取りを行う  
トラフィックの流れとしては  
リクエスト→Nginx→タスク管理用API→mysql  

_rolegetdep以外の[yamlファイル]のみでアプリケーションは起動するはず_  
APIサーバやSQL,Nginxのイメージは必須.  

認証・認可はIstioとAuth0を用いて実装  
発行元が確かなjwtとユーザロールを所持していなければ,使用できるHTTPメソッドが制限される

### db-dep.yaml  
nginxイメージを利用したpod nginx.confは__dbconf.yaml__に記述している  
主にapiサーバが提供するエンドポイントごとの処理が記述されている  
プロキシ先が/authpointの場合のみ適切なjwtを用いずにアクセス可能  

### fastapidep2.yaml  
自作apiサーバのイメージからなるpod　fastapiserverにてイメージ元のディレクトリを置いている  
routersではアクセスポイントごとの振る舞いを記述し,serviceで具体的な処理を記述　　
/authpointではAuthorizationcodeを用いてアクセストークンを取得する,取得できれば/userindexに遷移してアプリケーションの画面が表示される


