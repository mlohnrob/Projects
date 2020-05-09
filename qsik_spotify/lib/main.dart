import 'package:flutter/material.dart';
import 'package:qsik/locator.dart';
import 'package:qsik/services/dialog_service.dart';
import 'package:qsik/services/navigation_service.dart';
import 'package:qsik/ui/router.dart';
import 'package:qsik/ui/views/startup/startup_view.dart';

import 'managers/dialog_manager.dart';

void main() {
  setupLocator();
  runApp(Qsik());
}

class Qsik extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Qsik",
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
