import 'package:flutter/material.dart';
import 'package:qsik_spotify/locator.dart';
import 'package:qsik_spotify/services/dialog_service.dart';
import 'package:qsik_spotify/services/navigation_service.dart';
import 'package:qsik_spotify/ui/router.dart';
import 'package:qsik_spotify/ui/views/startup/startup_view.dart';

import 'managers/dialog_manager.dart';

void main() {
  setupLocator();
  runApp(QsikSpot());
}

class QsikSpot extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "qsik_spotify",
      builder: (context, child) => Navigator(
        key: locator<DialogService>().dialogNavigationKey,
        onGenerateRoute: (settings) => MaterialPageRoute(builder: (context) => DialogManager(child: child)),
      ),
      navigatorKey: locator<NavigationService>().navigationkey,
      home: StartUpView(),
      onGenerateRoute: generateRoute,
    );
  }
}
