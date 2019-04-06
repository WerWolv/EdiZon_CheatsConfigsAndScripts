# Celeste
Format is the same on all platforms. XML document:
```xml
<?xml version="1.0"?>
<SaveData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <Version>1.2.6.1</Version> <!-- Last version used -->
  <Name>Madeline</Name> <!-- Save name -->
  <Time>2175643340000</Time> <!-- Save time in seconds * 10000000 (unsure of unit name) -->
  <LastSave>0001-01-01T00:00:00</LastSave> <!-- Unused? -->
  <CheatMode>true</CheatMode> <!-- Cheat mode stamp -->
  <AssistMode>false</AssistMode> <!-- Assist mode -->
  <VariantMode>true</VariantMode> <!-- Variant mode (added in update not yet released for Switch) -->
  <Assists> <!-- should be self explanatory, **also used for variant mode** -->
    <GameSpeed>10</GameSpeed>
    <Invincible>false</Invincible>
    <DashMode>Normal</DashMode>
    <InfiniteStamina>false</InfiniteStamina>
    <MirrorMode>false</MirrorMode>
    <!-- variants -->
    <ThreeSixtyDashing>true</ThreeSixtyDashing>
    <InvisibleMotion>false</InvisibleMotion>
    <NoGrabbing>false</NoGrabbing>
    <LowFriction>false</LowFriction>
    <SuperDashing>false</SuperDashing>
    <Hiccups>false</Hiccups>
    <PlayAsBadeline>false</PlayAsBadeline>
  </Assists>
  <TheoSisterName>Alex</TheoSisterName> <!-- Alex by default, Maddy if file name is Alex -->
  <UnlockedAreas>9</UnlockedAreas> <!-- Unlocked areas, doesn't include prologue, does include epilogue -->
  <TotalDeaths>18256</TotalDeaths>
  <TotalStrawberries>84</TotalStrawberries>
  <TotalGoldenStrawberries>1</TotalGoldenStrawberries>
  <TotalJumps>49845</TotalJumps>
  <TotalWallJumps>13858</TotalWallJumps>
  <TotalDashes>64213</TotalDashes>
  <Flags> <!-- changes ch2 and ch3 Theo cutscenes -->
    <string>MetTheo</string> <!-- set after talking to Theo -->
    <string>TheoKnowsName</string> <!-- set after talking to Theo in ch2 or ch3, or after second conversation in ch1 -->
  </Flags>
  <Poem> <!-- order of hearts in journal -->
    <string>os</string>
    <string>fc</string>
    <string>cs</string>
    <string>t</string>
    <string>mc</string>
    <string>fcr</string>
    <string>crr</string>
    <string>osr</string>
    <string>csr</string>
    <string>tr</string>
    <string>tf</string>
    <string>tfr</string>
    <string>tsr</string>
    <string>ts</string>
    <string>cr</string>
    <string>mcr</string>
  </Poem>
  <SummitGems> <!-- which gems in Summit are collected -->
    <boolean>true</boolean>
    <boolean>true</boolean>
    <boolean>true</boolean>
    <boolean>true</boolean>
    <boolean>true</boolean>
    <boolean>true</boolean>
  </SummitGems>
  <LastArea ID="7" Mode="CSide" SID="Celeste/7-Summit" /> <!-- self explanatory -->
  <!-- information on stats removed due to length, can be ignored or copied from 100% save -->
</SaveData>
```
