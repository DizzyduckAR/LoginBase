const functions = require("firebase-functions");

const admin = require("firebase-admin");
admin.initializeApp()
// On sign up.
exports.processSignUp = functions.auth.user().onCreate(user => {
  //data you wanna write
  const customClaims = {
      "NickName": "Free Pirate",
      "Time": "Free",
      "Token": "Free"
  };
  return admin
    .auth()
    .setCustomUserClaims(user.uid, customClaims)
    .then(() => {
      // Update real-time database
      
      const metadataRef = admin.database().ref("Free/" + user.uid);
      return metadataRef.set(customClaims);
    })
    .catch(error => {
      console.log(error);
    });
});


exports.Login = functions.https.onRequest(async (req, res) => {
  const PCUID = req.query.UserPCUID;
  const snapshott = await admin.database().ref("Free/" + PCUID).once('value');

  const now= Date.now();
  const time2 = parseInt(now/(1000*60*60*24))

  if (snapshott === null) {

    res.status(200).json({
      Error: "No Account"
      });

  }
  else {
    //const time2 = 18550
    const time = snapshott.val().Time
    const NickNameP = snapshott.val().NickName
    const TokenP = snapshott.val().Token


    if (time === "Free") {
      res.status(200).json({
        Nick: NickNameP,
        Time: time,
        Token: TokenP,
        });
        
    }

    else if (time === "Life") {
      res.status(200).json({
        Nick: NickNameP,
        Time: time,
        Token: TokenP,
        });
        
    }

    else if (time < time2) {
        //var metadataRef2 = await admin.database().ref("Free/" + PCUID + '/NickName').set('Test');
        const db = admin.database();
        const ref = db.ref("Free/" + PCUID)
        await ref.update({
            "Time": "Free"
        });
        res.status(200).json({
          Nick: NickNameP,
          Time: "Free",
          Token: TokenP,
          });
         
    
    }  
    else {
      //var days = 
      const days = time - time2
      res.status(200).json({
        Nick: snapshott.val().NickName,
        Time: days+" days",
        Token: TokenP,
        });

    }
    
    
      
  }
  
  
});



exports.getTrail = functions.https.onRequest(async (req, res) => {
  const PCUID = req.query.UserPCUID;
  const snapshott = await admin.database().ref("Free/" + PCUID).once('value');
  if (snapshott === null) {
    res.status(200).json({
      Error: "No Account"
      });

  }
  else {
    const now= Date.now();
    const time2 = parseInt(now/(1000*60*60*24))
    const time = snapshott.val().Time
    const NickNameP = snapshott.val().NickName
    //const TokenP = snapshott.val().Token
    
    if (time === "Free") {
        const time = time2 + 90 ;
        const days = time - time2
        const db = admin.database();
        const ref = db.ref("Free/" + PCUID)

        await ref.update({
            "Time": time,
            "Token": "Tester",
        });
        res.status(200).json({
          Nick: NickNameP,
          Time: days+' Days',
          Token: "Tester",
          });
        
    }
     
    
    else{
      res.status(200).json({
        Error: "No Free Account"
        });
    }
      
  }
  
});

exports.SetNick = functions.https.onRequest(async (req, res) => {
  const PCUID = req.query.UserPCUID;
  const NickSet = req.query.NickSet;
  const snapshott = await admin.database().ref("Free/" + PCUID).once('value');
  if (snapshott === null) {
    res.status(200).json({
      Error: "No Account"
      });

  }
  else {

    const db = admin.database();
    const ref = db.ref("Free/" + PCUID)

    await ref.update({
        "NickName": NickSet,
    });
    
      res.status(200).json({
        Error: "No Free Account"
        });
    }
      
  
  
});