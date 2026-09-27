# Cursor Finder privacy

Effective September 27, 2026. Applies to Cursor Finder 1.1 and later.

Cursor Finder uses the pointer position and your chosen shortcut locally to display effects. It does not record keystroke history, capture screen contents or upload pointer activity. Preferences, installed effects, blocked creators and a locally generated creator identifier are stored on your Mac. The app has no account system, advertising, analytics or crash-reporting service.

## Network connections

When you open or refresh Effect Gallery, the app downloads a shared catalog from GitHub's `raw.githubusercontent.com` service over HTTPS. It sends no creator identifier, installed-effect list, pointer activity or preferences with this request. A cached catalog and bundled examples are available if the request fails.

The direct-download edition uses Sparkle to check for updates and download signed releases from GitHub. Automatic checks can be managed in the app's update settings. Sparkle's optional system-profile reporting is disabled. The App Store edition does not include Sparkle; Apple manages its updates.

GitHub receives ordinary request information, such as the connection's IP address and HTTP headers, when hosting the catalog, update feed and downloads. GitHub processes that information under its [privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). Cursor Finder's developer does not operate a separate telemetry server.

## Sharing and support

Exporting an effect writes a file only to the location you choose. Submitting to the gallery opens GitHub in your browser; you choose whether to upload the file and send the submission. GitHub submissions are public and include the effect data, chosen creator name, credits and your GitHub account identity. Do not include personal information you do not want to publish.

Reports open your mail application with the effect name and identifier. Nothing is sent until you send the email. The developer uses received support emails and gallery submissions to respond, review content and operate the gallery. Contact **mangocandy.studio@gmail.com** for support or a request concerning your submitted information. Removal from this catalog cannot retract copies already downloaded or shared by others.

Locally created effects can be deleted from My Effects. For a public gallery entry, contact the support address or open an issue to request removal. Changes to this policy will be published here with an updated effective date.
