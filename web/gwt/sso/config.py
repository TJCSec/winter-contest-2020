import os

class Config(object):
  SECRET_KEY = os.getenv("SECRET_KEY") or b"\x89\xb5`\xd5X\xab\nTsl15#\x97\x17 #\x99\xbd\xe4\xc0\xbf\x18\x9b\x14\x14\xb5\xe8\xd1\x9f\t\x1b-\xf5*\x07\xaf\x06[\xedfw\x99'V\xc2\x19\xfbC\x90\xd8\xc2\x15\xc9WhI\x81\xb4\x14\xd4\x8f\xa4\x99"
  SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI") or "postgres://gwt:cjwU2eFvvg0qtI0hz%2B8Dpyk%2FnyHKj1D5jE9%2Fb3CIKU4%3D@localhost/gwt"
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  RSA_N = int(os.getenv("RSA_N") or 412374444232529820507274042347105419957072249563428251165479008204399618024448941404689816607501076459087379572933226218906633160777502045481491615562655374432349625278504976700974614623698306871015020605545343149210005904086075466486952047741445824001796451053385302266990862829255520098670941528925624965241227631957202791362056629569525580805524800500327737055011161062666902286002355088242959060145672939586117453375529208379324252635456781311635642306788003531266175428493624401036061509852971993499761849645006574568205253400693028895784309568089749024980352369462333442312196640666855999571155683651633129653637656654878393888379144632421789403084381598408213507751424448896464251923741266933283065057152074444514964140109138112069209065000012151202488341455065940701688308853384137334685687690272819778454246041978791094308759558589952829863143673061160620221272378695787590682832146464691512537700169046245310045613475358528262011317760226795883983770882379711214207273334350895864758677817721412618229477254384291543852948892718463194519055705088200679493652394005523340571662215354900313802049764981279470635990936981716448744427635516016913225141914855873636355668913055105593751900087479055263485210282773509072906073511)
  RSA_E = int(os.getenv("RSA_E") or 65537)
  RSA_D = int(os.getenv("RSA_D") or 16624094506345175790472832443979012153845688440828500535257877835055370108802571115418626050582386194133220269949640411833793503071153095261640002568267322264526415764923785776644871322089978588480120915511097496074169333332246080572173387706683245601915654114210964319230203695544396052622009361420594491022892769025602785827525727685470598051302264719499914266740001640715411993829717901996397421867111218187993382544488581542307012458044720024190020400301110904216018973741247778621805613760647451162341437764348495811666665845013213640274381584126418922501763751165288080848815532060390825806292526606460697446401312080348464818423763504623461835482462911921569783590328389941360038341095671192506964212651906309479230623105776304730305075876072368807965929480882354100046386672961412421970275348947383396132156461411224569145023933698712429627211669387846768415959917528841673412445335626918668312038815923041658866693172788525513245269201191648238378816125229953242158858835401178924896597588562605662419015276299100468284332466070915249625090703063679540296593490391395003564987208332282076891716590850090775829994421567503609562163571384171357531712584334262806190480913218114147864440524141727192397861923406065311514995025)
